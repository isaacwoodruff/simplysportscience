import json
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


stripe.api_key = settings.STRIPE_SECRET
STRIPE_PUBLISHABLE = settings.STRIPE_PUBLISHABLE
ENDPOINT_SECRET = settings.ENDPOINT_SECRET


@login_required
def checkout_view(request):
    user = request.user.email
    session = stripe.checkout.Session.create(
        client_reference_id=user,
        payment_method_types=['card'],
        line_items=[{
            'name': 'Job Post',
            'amount': 10000,
            'currency': 'eur',
            'quantity': 1,
        }],
        success_url='https://simplysportscience.herokuapp.com/checkout/payment-success/',
        cancel_url='https://simplysportscience.herokuapp.com/checkout/payment-failed/',
    )
    session_id = session.id

    context = {
        "page_title": "Checkout",
        "STRIPE_PUBLISHABLE": STRIPE_PUBLISHABLE,
        "session_id": session_id,
    }
    return render(request, "checkout.html", context)


@login_required
def credit_user(customer_email):
    profile = User.objects.get(email__iexact=customer_email)
    profile.credits += 1
    profile.save()


@csrf_exempt
def webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, ENDPOINT_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session['customer']
        credit_user(customer_email)

    return HttpResponse(status=200)


def success_view(request):
    render(request, "payment-status.html", {"payment_status": "Payment Success"})

def fail_view(request):
    render(request, "payment-status.html", {"payment_status": "Payment Failed"})
