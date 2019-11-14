from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployerRegistrationForm, CandidateRegistrationForm

def register(request, title):
    if request.method == "POST":
        if title == "employers":
            form = EmployerRegistrationForm(request.POST)
        elif title == "candidates":
            form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.username = form.cleaned_data.get("email")
            form_obj.save()
            messages.success(request, "Success! Your account is now created.")
    else:
        if title == "employers":
            form = EmployerRegistrationForm()
        elif title == "candidates":
            form = CandidateRegistrationForm()
            
    context = {
        "form" : form,
        "page_title" : title.capitalize(),
    }
    return render(request, "register.html", context)