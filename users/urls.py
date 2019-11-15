from django.urls import path
from .views import register_employer, register_candidate

urlpatterns = [
    path('register/employer', register_employer, name="register_employer"),
    path('register/candidate', register_candidate, name="register_candidate"),
]
