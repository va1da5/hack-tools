from django.conf import settings
from prometheus_client import push_to_gateway as push_to_remote

from .registry import REGISTRY


def push_to_gateway():
    push_gateway_host = getattr(settings, "PROMETHEUS_PUSH_GATEWAY_HOST")
    push_to_remote(push_gateway_host, job="celery", registry=REGISTRY)
