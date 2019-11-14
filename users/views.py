from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployerRegistrationForm, CandidateRegistrationForm

def register(request, title="Register"):
    if request.method == "POST":
        if title == "employers":
            form = EmployerRegistrationForm(request.POST)
            name = form.cleaned_data.get("employer")
        elif title == "candidates":
            form = CandidateRegistrationForm(request.POST)
            name = form.cleaned_data.get("first_name")
        if form.is_valid():
            form.save()
            messages.success(request, f"Success! Welcome aboard {name}")
    else:
        if title == "employers":
            form = EmployerRegistrationForm()
        elif title == "candidates":
            form = CandidateRegistrationForm()
    return render(request, "register.html", {"form" : form})