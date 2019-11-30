import stripe
from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


stripe.api_key = settings.STRIPE_SECRET
STRIPE_PUBLISHABLE = settings.STRIPE_PUBLISHABLE
ENDPOINT_SECRET = settings.ENDPOINT_SECRET


@login_required
def checkout_view(request):
    '''
    This view creates the session object necessary to fulfill the user order.
    The email of the current user is assigned to the client_reference_id to uniquely
    identify the user for order confirmation in the webhook.
    '''
    user = request.user.email
    session = stripe.checkout.Session.create(
        client_reference_id=user,
        payment_method_types=['card'],
        line_items=[{
            'name': 'Job Post',
            'description': 'One job post',
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


def credit_user(customer_email):
    '''
    Finds the user with the customer_email and credits their account
    '''
    user = User.objects.get(email__iexact=customer_email)
    user.employerprofile.credits += 1
    user.employerprofile.save()


@csrf_exempt
def webhook_view(request):
    '''
    This view is modified from the one provided in the Stripe documentation.
    The @csrf_exempt and sig_header prevent django from returning a security error, which
    allows Stripe API to access the webhook. An event object is created using the
    ENDPOINT_SECRET environment variable provided by Stripe. if the checkout was 
    successful session object is extracted from the event object and the client_reference_id
    is taken from it to uniquely identify the user that paid. A function, credit_user(), is 
    called with the id to credit the users account.
    '''
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
        customer_email = session['client_reference_id']
        credit_user(customer_email)

    return HttpResponse(status=200)


def success_view(request):
    return render(request, "payment-status.html", {"payment_status": "Payment Success"})


def fail_view(request):
    return render(request, "payment-status.html", {"payment_status": "Payment Failed"})
