from celery import shared_task
from hacker_tools.metrics.celery.metrics import metrics

from . import services


@shared_task
def nmap_scan(host: str) -> str:
    output = services.nmap_scan(host=host)
    metrics.nmap_scans.inc()
    return output


@shared_task(bind=True)
def track_job(self, task_id):
    finished = services.track_job(task_id=task_id)
    if not finished:
        self.retry(countdown=2, max_retries=300)
