from django.urls import path
from .views import jobs_view

urlpatterns = [
    path('', jobs_view, name="jobs"),
]
