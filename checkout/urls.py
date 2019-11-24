from django.urls import path
from checkout.views import checkout_view, charge_view

urlpatterns = [
    path('', checkout_view, name="checkout"),
    path('charge/', charge_view, name='charge'),
]
