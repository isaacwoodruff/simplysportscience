import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


stripe.api_key = settings.STRIPE_SECRET
STRIPE_PUBLISHABLE = settings.STRIPE_PUBLISHABLE


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
