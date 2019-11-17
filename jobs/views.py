from django.shortcuts import render, get_object_or_404
from .models import Job

def job_list(request):
    context = {
        "page_title" : "Jobs",
        "posts" : Job.objects.all(),
    }
    return render(request, "job-list.html", context)

def job_details(request, pk, slug):
    job_post = get_object_or_404(Job, pk=pk)

    context = {
        "page_title" : job_post.title,
        "post" : job_post,
    }
    return render(request, "job-details.html", context)