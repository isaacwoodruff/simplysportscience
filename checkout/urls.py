from django.urls import path
from checkout.views import checkout_view, credit_view

urlpatterns = [
    path('', checkout_view, name="checkout"),
    path('router/', credit_view, name="credit_view"),
    path('webhook/', credit_view, name="credit_view"),
]
