from django.urls import path
from search import views as search_views

urlpatterns = [
    path('', search_views.job_list, name="jobs"),
    path('<pk>/', search_views.employer_job_list, name="employer_job_list"),
    path('<slug:slug>/<pk>/', search_views.employer_job_list, name="employer_job_list"),
]
