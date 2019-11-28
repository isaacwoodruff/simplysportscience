from django.urls import path
from search import views as search_views

urlpatterns = [
    path('', search_views.job_list, name="jobs"),
    path('jobs/', search_views.job_list, name="jobs"),
    path('jobs/results/', search_views.search_results, name="search_results"),
    path('ajax-search/', search_views.autocomplete_title_search, name="autocomplete_title_search"),
    path('employment/', search_views.employment_type_job_list, name="employment_type_job_list"),
    path('location/', search_views.location_job_list, name="location_job_list"),
    path('employer/<pk>/', search_views.employer_job_list, name="employer_job_list"),
    path('employer/<slug:slug>/<pk>/', search_views.employer_job_list, name="employer_job_list"),
]
