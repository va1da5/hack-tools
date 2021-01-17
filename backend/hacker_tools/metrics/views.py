import os

import prometheus_client
from django.http import HttpResponse
from prometheus_client import multiprocess

from celery.__main__ import main


def metrics(request):
    if "prometheus_multiproc_dir" in os.environ:
        registry = prometheus_client.CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
    else:
        registry = prometheus_client.REGISTRY
    metrics_page = prometheus_client.generate_latest(registry)
    return HttpResponse(metrics_page, content_type=prometheus_client.CONTENT_TYPE_LATEST)
