import os
from django.shortcuts import render, get_object_or_404
from jobs.models import Job, EmployerProfile

def job_list(request):
    context = {
        "page_title": "Jobs",
        "posts": Job.objects.all(),
        "ALGOLIA_PUBLIC_KEY": os.environ.get('ALGOLIA_PUBLIC_KEY'),
        "ALGOLIA_PUBLIC_APP_ID": os.environ.get('ALGOLIA_PUBLIC_APP_ID'),
    }
    return render(request, "job-list.html", context)

def employer_job_list(request, pk, slug=""):
    employer_object = get_object_or_404(EmployerProfile, pk=pk)

    context = {
        "page_title": employer_object.company_name + " " + "Jobs",
        "posts": Job.objects.filter(employer_fk=employer_object),
        "ALGOLIA_PUBLIC_KEY": os.environ.get('ALGOLIA_PUBLIC_KEY'),
        "ALGOLIA_PUBLIC_APP_ID": os.environ.get('ALGOLIA_PUBLIC_APP_ID'),
    }
    return render(request, "job-list.html", context)
