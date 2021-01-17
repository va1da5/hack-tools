from hacker_tools.metrics.config import NAMESPACE
from prometheus_client import Counter

from ..config import NAMESPACE
from ..metrics import Metrics
from .registry import REGISTRY


class CeleryMetrics(Metrics):
    def register(self):

        self.celery_tasks_by_status = self.register_metric(
            Counter,
            "celery_tasks_by_status",
            "Celery tasks by status",
            ["status"],
            namespace=NAMESPACE,
            registry=REGISTRY,
        )

        self.nmap_scans = self.register_metric(
            Counter,
            "nmap_scans",
            "NMAP Scans",
            namespace=NAMESPACE,
            registry=REGISTRY,
        )


metrics = CeleryMetrics.get_instance()
