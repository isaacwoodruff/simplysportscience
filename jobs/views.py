import os
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobPostForm
from django.contrib.auth.models import User

'''
Renders details of a specific job post
'''


def job_details(request, pk, slug=""):
    post = get_object_or_404(Job, pk=pk)

    context = {
        "page_title": post.title,
        "post": post,
    }
    return render(request, "job-details.html", context)


'''
If an employer has credits this creates a new job post.
Assigns the hidden form field 'employer' the company_name of the current user.
Creates a slug for the hidden slug field from the form title.
After saving it finds the new job post in the database and redirects to it.
Algolia keys are for the Algolia API location autofill field in the form
'''
@login_required
def new_job(request):
    if request.method == "POST":
        form = JobPostForm(request.POST)
        profile = request.user.employerprofile

        if form.is_valid() and profile.credits > 0:
            form_obj = form.save(commit=False)
            employer_user = request.user.employerprofile
            form_obj.employer_fk = employer_user
            form_obj.employer = employer_user.company_name

            form_obj.slug = slugify(form.cleaned_data.get("title"))
            form_obj.save()

            messages.success(
                request, "Success! Your new job post has been created.")

            profile.credits -= 1
            profile.save()

            new_job_object = Job.objects.get(pk=form_obj.pk)
            return redirect(new_job_object)
        else:
            messages.warning(
                request, "You don't have any credits! Click Buy More at the bottom of the page.")
    else:
        form = JobPostForm()

    context = {
        "page_title": "Create a new job",
        "new_job_form": form,
        "ALGOLIA_PUBLIC_KEY": os.environ.get('ALGOLIA_PUBLIC_KEY'),
        "ALGOLIA_PUBLIC_APP_ID": os.environ.get('ALGOLIA_PUBLIC_APP_ID'),
    }
    return render(request, "new-job.html", context)


def credit_amount_view(request):
    '''
    Takes ajax request and finds the logged user profile
    Then sends the amount of credit that profile has as a JSON response for feedback to the user.
    '''
    if request.is_ajax():
        user = User.objects.get(username=request.user.username)
        credit_amount = user.employerprofile.credits
        data = {'result': 'success', 'credit_amount': credit_amount}
    return JsonResponse(data)
