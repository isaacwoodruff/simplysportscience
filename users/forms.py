from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmployerProfile


class EmployerRegistrationForm(UserCreationForm):
    '''
    The Employer and Candidate registration forms hide the username field. These are then
    filled in the view with the email of the user.
    '''
    email = forms.EmailField()
    company_name = forms.CharField(max_length=200)
    username = forms.EmailField(required=False)
    username.widget = username.hidden_widget()

    class Meta:
        model = User
        fields = ["company_name", "email", "password1", "password2"]


class EmployerUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.EmailField(required=False)
    username.widget = username.hidden_widget()

    class Meta:
        model = User
        fields = ["email"]


class EmployerProfileUpdateForm(forms.ModelForm):
    slug = forms.SlugField(required=False)
    slug.widget = slug.hidden_widget()
    class Meta:
        model = EmployerProfile
        fields = ["company_name"]


class CandidateRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.EmailField(required=False)
    username.widget = username.hidden_widget()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]


class CandidateUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.EmailField(required=False)
    username.widget = username.hidden_widget()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=50, widget=forms.EmailInput)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password"]
