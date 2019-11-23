from django.shortcuts import render

def checkout_view(request):
    context = {
        "page_title": "Checkout",
    }
    return render(request, "checkout.html", context)