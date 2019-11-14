from django.urls import path
from .views import register

urlpatterns = [
    path('register/<title>', register, name="register"),
]
