from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from . import services


class ScanAPI(APIView):
    def get(self, request):
        return Response(services.get_jobs())

    def post(self, request):
        host = request.data.get("host")
        if not host:
            raise exceptions.ValidationError("Missing 'host' field")
        job_id = services.start_scan(host=host)
        return Response({"id": job_id})


class ScanDetailsAPI(APIView):
    def get(self, request, uuid):
        try:
            return Response(services.get_job_details(job_id=uuid))
        except:
            raise exceptions.NotFound()


class ScanResultsAPI(APIView):
    def get(self, request, uuid):
        try:
            return Response(services.get_job_result(job_id=uuid))
        except:
            raise exceptions.NotFound()
