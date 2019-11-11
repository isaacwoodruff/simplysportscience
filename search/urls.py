from django.urls import path
from .views import search_view

urlpatterns = [
    path('jobs/', search_view, name="jobs-search"),
]
