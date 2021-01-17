from django.utils.deprecation import MiddlewareMixin
from prometheus_client import Counter

from .metrics import Metrics


class PrometheusAfterMiddleware(MiddlewareMixin):
    """Monitoring middleware that should run after other middlewares."""

    metrics_cls = Metrics

    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.metrics = self.metrics_cls.get_instance()

    def _method(self, request):
        m = request.method
        if m not in (
            "GET",
            "HEAD",
            "POST",
            "PUT",
            "DELETE",
            "TRACE",
            "OPTIONS",
            "CONNECT",
            "PATCH",
        ):
            return "<invalid method>"
        return m

    def label_metric(self, metric, request, response=None, **labels):
        return metric.labels(**labels) if labels else metric

    def process_request(self, request):
        method = self._method(request)
        self.label_metric(self.metrics.requests_by_method, request, method=method).inc()
