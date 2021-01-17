from celery.signals import (
    task_failure,
    task_postrun,
    task_retry,
    task_revoked,
    task_success,
    worker_ready,
)

from .export import push_to_gateway
from .metrics import metrics
from .server import start_metrics_server


@task_success.connect
def capture_task_success(*args, **kwargs):
    metrics.celery_tasks_by_status.labels(status="success").inc()


@task_retry.connect
def capture_task_retry(*args, **kwargs):
    metrics.celery_tasks_by_status.labels(status="retry").inc()


@task_failure.connect
def capture_task_failure(*args, **kwargs):
    metrics.celery_tasks_by_status.labels(status="failure").inc()


@task_revoked.connect
def capture_task_revoked(*args, **kwargs):
    metrics.celery_tasks_by_status.labels(status="revoked").inc()


# @task_postrun.connect
# def capture_task_postrun(*args, **kwargs):
#     push_to_gateway()


@worker_ready.connect
def worker_ready(*args, **kwargs):
    start_metrics_server()
