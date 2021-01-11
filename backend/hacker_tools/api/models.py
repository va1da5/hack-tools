from django.db import models


class Scan(models.Model):
    CELERY_STATES = [
        ("PENDING", "waiting for execution or unknown task id"),
        ("STARTED", "task has been started"),
        ("SUCCESS", "task executed successfully"),
        ("FAILURE", "task execution resulted in exception"),
        ("RETRY", "task is being retried"),
        ("REVOKED", "task has been revoked"),
    ]

    uuid = models.UUIDField(verbose_name="Scan ID", unique=True)
    host = models.CharField(max_length=50, verbose_name="Host Value")
    state = models.CharField(
        max_length=8,
        choices=CELERY_STATES,
        default="PENDING",
        verbose_name="Scan Status",
    )
    output = models.TextField(verbose_name="Scan Output")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
