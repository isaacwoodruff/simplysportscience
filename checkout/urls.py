from django.urls import path
from checkout.views import checkout_view

urlpatterns = [
    path('', checkout_view, name="jobs"),
]
