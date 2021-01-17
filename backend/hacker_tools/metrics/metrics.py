from prometheus_client import Counter

from .config import NAMESPACE


class Metrics:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def label_metric(self, metric, **labels):
        return metric.labels(**labels) if labels else metric

    def register_metric(self, metric_cls, name, documentation, labelnames=(), **kwargs):
        return metric_cls(name, documentation, labelnames=labelnames, **kwargs)

    def __init__(self, *args, **kwargs):
        self.register()

    def register(self):
        self.requests_by_method = self.register_metric(
            Counter,
            "api_http_requests_total_by_method",
            "Count of requests by method.",
            ["method"],
            namespace=NAMESPACE,
        )
