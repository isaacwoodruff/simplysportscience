from django.urls import path
from checkout.views import checkout_view, credit_view, webhook_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', checkout_view, name="checkout"),
    path('webhook/', csrf_exempt(webhook_view), name="webhook_view"),
]
