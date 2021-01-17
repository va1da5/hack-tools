import os

import prometheus_client
from prometheus_client import multiprocess, start_http_server

from .registry import REGISTRY


def start_metrics_server():
    print("Metrics server started")
    if "prometheus_multiproc_dir" in os.environ:
        registry = prometheus_client.CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
    else:
        registry = REGISTRY
    start_http_server(9090, addr="0.0.0.0", registry=registry)
