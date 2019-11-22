from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users import forms as user_forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login

def register_choice(request):
    context = {
        "choice" : "choice",
        "page_title" : "Register",
    }
    return render(request, "register.html", context)

def register_employer(request):
    if request.method == "POST":
        form = user_forms.EmployerRegistrationForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.username = form.cleaned_data.get("email")
            form_obj.save()

            profile = User.objects.filter(
                username=form_obj.username).first().employerprofile
            profile.is_employer = True
            profile.company_name = form.cleaned_data.get("company_name")
            profile.save()

            messages.success(
                request, "Success! Your account has been created.")

            new_user = authenticate(username=form.cleaned_data["email"],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
    else:
        form = user_forms.EmployerRegistrationForm()

    context = {
        "form": form,
        "page_title": "For Employers",
    }
    return render(request, "register.html", context)


def register_candidate(request):
    if request.method == "POST":
        form = user_forms.CandidateRegistrationForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.username = form.cleaned_data.get("email")
            form_obj.save()

            profile = User.objects.filter(
                username=form_obj.username).first().candidateprofile
            profile.is_candidate = True
            profile.first_name = form.cleaned_data.get("first_name")
            profile.last_name = form.cleaned_data.get("last_name")
            profile.save()

            messages.success(
                request, "Success! Your account has been created.")

            new_user = authenticate(username=form.cleaned_data["email"],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
    else:
        form = user_forms.CandidateRegistrationForm()

    context = {
        "form": form,
        "page_title": "For Candidates",
    }
    return render(request, "register.html", context)


def login_view(request):
    if request.method == "POST":
        form = user_forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["email"],
                                    password=form.cleaned_data['password'],
                                )
            if user:
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                redirect(logged_user_type)
            else:
                messages.warning(request, "Your password/email is incorrect")
    else:
        form = user_forms.LoginForm()

    context = {
        "form": form,
        "page_title": "Log In",
    }
    return render(request, "login.html", context)

def logged_user_type(request):
    try:
        request.user.employerprofile
    except ObjectDoesNotExist:
        user_type = 'candidate_profile'
    else:
        user_type = 'employer_profile'

    return redirect(user_type)


@login_required
def employer_profile(request):
    update_form = user_forms.EmployerUpdateForm()
    profile_form = user_forms.EmployerProfileUpdateForm()

    context = {
        "update_form": update_form,
        "profile_form": profile_form,
    }

    return render(request, "profile.html", context)

@login_required
def candidate_profile(request):
    update_form = user_forms.CandidateUpdateForm()

    context = {
        "update_form": update_form,
    }

    return render(request, "profile.html", context)
