import subprocess
from typing import List, Mapping

from celery.result import AsyncResult, allow_join_result
from config.celery import app as celery_app

from . import tasks
from .models import Scan
from .serializers import ScanSerializer


def get_scans() -> List[Mapping[str, str]]:
    scans = Scan.objects.order_by("-updated_at").all()
    return [ScanSerializer(scan).data for scan in scans]


def get_scan_details(*, task_id: str) -> Mapping[str, str]:
    scan = Scan.objects.get(uuid=task_id)
    return ScanSerializer(scan).data


def cancel_scan(*, task_id: str) -> Mapping[str, str]:
    task_result = AsyncResult(task_id, app=celery_app)
    task_result.revoke(terminate=True)
    scan = Scan.objects.get(uuid=task_id)
    scan.state = task_result.state
    scan.save()
    return ScanSerializer(scan).data


def get_scan_result(*, task_id: str) -> str:
    scan = Scan.objects.get(uuid=task_id)
    return scan.output


def start_scan(*, host: str = None) -> Mapping[str, str]:
    task_result = tasks.nmap_scan.delay(host)
    scan = Scan(uuid=task_result.id, host=host)
    scan.save()
    tasks.track_job.delay(task_result.id)
    return ScanSerializer(scan).data


def nmap_scan(*, host: str = None) -> str:
    process = subprocess.Popen(
        ["nmap", "-F", "-sV", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if len(stderr):
        return stderr.decode()
    return stdout.decode()


def track_job(*, task_id: str) -> bool:
    task_result = AsyncResult(task_id, app=celery_app)
    scan = Scan.objects.get(uuid=task_id)
    scan.state = task_result.state
    finished = task_result.ready()
    if finished:
        with allow_join_result():
            scan.output = task_result.get()
    scan.save()
    return finished
