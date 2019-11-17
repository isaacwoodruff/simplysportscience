from django.shortcuts import render
from django.http import HttpResponse
from .models import Job

def job_list(request):
    context = {
        "page_title" : "Jobs",
        "posts" : Job.objects.all(),
    }
    return render(request, "job-list.html", context)

def job_details(request, job_pk):
    job_post = Job.objects.get(pk=job_pk)

    context = {
        "page_title" : job_post.title,
        "post" : job_post,
    }
    return render(request, "job-details.html", context)