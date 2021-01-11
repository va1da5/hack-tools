from django.urls import path

from . import views

urlpatterns = [
    path("scan/<str:task_id>/result/", views.ScanResultsAPI.as_view()),
    path("scan/<str:task_id>/", views.ScanDetailsAPI.as_view()),
    path("scan/", views.ScanAPI.as_view()),
]
