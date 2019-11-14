from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmployerRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    company_name = forms.CharField(max_length=200)
    username = forms.EmailField(required=False)
    username.widget = username.hidden_widget()

    class Meta:
        model = User
        fields = ["company_name", "email", "password1", "password2"]

class CandidateRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.EmailField(required=False)
    username.widget = username.hidden_widget()

    class Meta:
        model = User
        fields = ["first_name","last_name", "email", "password1", "password2"]