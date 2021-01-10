import subprocess
from typing import List, Mapping

from celery.result import AsyncResult, allow_join_result
from config.celery import app as celery_app

from . import tasks
from .models import Job
from .serializers import JobSerializer


def get_jobs() -> List[Mapping[str, str]]:
    jobs = Job.objects.order_by("-updated_at").all()
    return [JobSerializer(job).data for job in jobs]


def get_job_details(*, job_id: str) -> Mapping[str, str]:
    job = Job.objects.get(uuid=job_id)
    return JobSerializer(job).data


def get_job_result(*, job_id: str) -> str:
    job = Job.objects.get(uuid=job_id)
    return job.output


def start_scan(*, host: str = None) -> Mapping[str, str]:
    task_result = tasks.nmap_scan.delay(host)
    job = Job(uuid=task_result.id, host=host)
    job.save()
    tasks.track_job.delay(task_result.id)
    return JobSerializer(job).data


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
    job = Job.objects.get(uuid=task_id)
    job.state = task_result.state
    finished = task_result.ready()
    if finished:
        with allow_join_result():
            job.output = task_result.get()
    job.save()
    return finished
