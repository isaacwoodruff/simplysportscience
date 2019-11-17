from django import forms
from .models import Job

class JobPostForm(forms.ModelForm):
    employment_type = forms.ChoiceField
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea)
    requirements = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(max_length=100, required=True)
    employer = forms.CharField(default="test_company")
    slug = forms.SlugField(default="")
    slug.widget = slug.hidden_widget()

    class Meta:
        model = Job
        fields = ["title", "location", "employment_type", "description", "requirements"]
