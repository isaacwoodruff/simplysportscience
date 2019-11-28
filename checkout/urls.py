from django.urls import path
from checkout.views import checkout_view, webhook_view, success_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', checkout_view, name="checkout"),
    path('payment-success/', success_view, name="success_view"),
    path('payment-failed/', success_view, name="fail_view"),
    path('webhook/', csrf_exempt(webhook_view), name="webhook_view"),
]
