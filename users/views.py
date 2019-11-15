from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployerRegistrationForm, CandidateRegistrationForm
from django.contrib.auth.models import User

def register_employer(request):
    if request.method == "POST":
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.username = form.cleaned_data.get("email")
            form_obj.save()

            profile = User.objects.filter(username=form_obj.username).first().employerprofile
            profile.is_employer = True
            profile.company_name = form.cleaned_data.get("company_name")
            profile.save()

            messages.success(request, "Success! Your account has been created.")
    else:
        form = EmployerRegistrationForm()
            
    context = {
        "form" : form,
        "page_title" : "For Employers",
    }
    return render(request, "register.html", context)


def register_candidate(request):
    if request.method == "POST":
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.username = form.cleaned_data.get("email")
            form_obj.save()

            profile = User.objects.filter(username=form_obj.username).first().candidateprofile
            profile.is_candidate = True
            profile.first_name = form.cleaned_data.get("first_name")
            profile.last_name = form.cleaned_data.get("last_name")
            profile.save()

            messages.success(request, "Success! Your account has been created.")
    else:
        form = CandidateRegistrationForm()
            
    context = {
        "form" : form,
        "page_title" : "For Candidates",
    }
    return render(request, "register.html", context)