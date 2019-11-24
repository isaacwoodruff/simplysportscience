from django.conf import settings
import stripe
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET
STRIPE_PUBLISHABLE = settings.STRIPE_PUBLISHABLE

def checkout_view(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'name': 'T-shirt',
            'description': 't-shirt',
            'amount': 500,
            'currency': 'usd',
            'quantity': 1,
        }],
        success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://example.com/cancel',
    )
    session_id = session.id
    
    context = {
        "page_title": "Checkout",
        "STRIPE_PUBLISHABLE": STRIPE_PUBLISHABLE,
        "session_id": session_id,
    }
    return render(request, "checkout.html", context)

def charge_view(request):
    return render(request, 'charge.html')
