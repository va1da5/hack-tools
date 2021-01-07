from django.urls import path

from . import views

urlpatterns = [
    path("scan/<str:uuid>/result/", views.ScanResultsAPI.as_view()),
    path("scan/<str:uuid>/", views.ScanDetailsAPI.as_view()),
    path("scan/", views.ScanAPI.as_view()),
]
