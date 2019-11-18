from django.urls import path
from jobs import views as job_views

urlpatterns = [
    path('', job_views.job_list, name="jobs"),
    path('<pk>/<slug:slug>', job_views.job_details, name="job_details"),
    path('new-job', job_views.new_job, name="new_job"),
]
