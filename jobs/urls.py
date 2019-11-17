from django.urls import path
from jobs import views as job_views

urlpatterns = [
    path('', job_views.job_list, name="jobs"),
    path('<job_pk>', job_views.job_details, name="job_details"),
]
