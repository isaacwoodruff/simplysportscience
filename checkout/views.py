import json
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


stripe.api_key = settings.STRIPE_SECRET
STRIPE_PUBLISHABLE = settings.STRIPE_PUBLISHABLE
ENDPOINT_SECRET = settings.ENDPOINT_SECRET


@login_required
def checkout_view(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'name': 'Job Post',
            'amount': 10000,
            'currency': 'eur',
            'quantity': 1,
        }],
        success_url='https://simplysportscience.herokuapp.com/checkout/router/',
        cancel_url='https://simplysportscience.herokuapp.com/jobs/search/',
    )
    session_id = session.id

    context = {
        "page_title": "Checkout",
        "STRIPE_PUBLISHABLE": STRIPE_PUBLISHABLE,
        "session_id": session_id,
    }
    return render(request, "checkout.html", context)


@login_required
def credit_view(request):
    profile = request.user.employerprofile
    profile.credits += 1
    profile.save()
    return redirect("new_job")


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

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object  # contains a stripe.PaymentIntent
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object  # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    # ... handle other event types
    else:
        # Unexpected event type
        return HttpResponse(status=400)

    return HttpResponse(status=200)
