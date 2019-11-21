from django.urls import path
from search import views as search_views

urlpatterns = [
    path('', search_views.job_list, name="jobs"),
    path('ajax-search/', search_views.autocomplete_title_search, name="autocomplete_title_search"),
    path('<pk>/', search_views.employer_job_list, name="employer_job_list"),
    path('<slug:slug>/<pk>/', search_views.employer_job_list, name="employer_job_list"),
    path('results', search_views.search_results, name="search_results"),
    path('employment', search_views.employment_type_job_list, name="employment_type_job_list"),
]
