from django.urls import path
from jobs import views as job_views

urlpatterns = [
    path('credit-amount/', job_views.credit_amount_view, name="credit_amount_view"),
    path('new-job/', job_views.new_job, name="new_job"),
    path('<pk>/', job_views.job_details, name="job_details"),
    path('<pk>/<slug:slug>/', job_views.job_details, name="job_details"),
]
