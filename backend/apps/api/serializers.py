from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    host = serializers.CharField(required=True, allow_blank=False, max_length=50)
    state = serializers.ChoiceField(choices=Job.CELERY_STATES)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()