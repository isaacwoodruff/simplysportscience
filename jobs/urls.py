from django.urls import path
from jobs import views as job_views

urlpatterns = [
    path('', job_views.job_list, name="jobs"),
    path('jobs/new-job/', job_views.new_job, name="new_job"),
    path('jobs/<pk>/', job_views.job_details, name="job_details"),
    path('jobs/<pk>/<slug:slug>/', job_views.job_details, name="job_details"),
    path('employer/<pk>/', job_views.employer_job_list, name="employer_job_list"),
    path('employer/<pk>/jobs/', job_views.employer_job_list, name="employer_job_list"),
    path('employer/<pk>/<slug:slug>/jobs/', job_views.employer_job_list, name="employer_job_list"),
]
