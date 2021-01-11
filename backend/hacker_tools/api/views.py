from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from . import services


class ScanAPI(APIView):
    def get(self, request):
        return Response(services.get_scans())

    def post(self, request):
        host = request.data.get("host")
        if not host:
            raise exceptions.ValidationError("Missing 'host' field")
        job = services.start_scan(host=host)
        return Response(job)


class ScanDetailsAPI(APIView):
    def get(self, request, task_id):
        try:
            return Response(services.get_scan_details(task_id=task_id))
        except:
            raise exceptions.NotFound()

    def delete(self, request, task_id):
        return Response(services.cancel_scan(task_id=task_id))


class ScanResultsAPI(APIView):
    def get(self, request, task_id):
        try:
            return Response(services.get_scan_result(task_id=task_id))
        except:
            raise exceptions.NotFound()
