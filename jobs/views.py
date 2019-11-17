from django.shortcuts import render
from django.http import HttpResponse
from .models import Job

def jobs_view(request):
    context = {
        "page_title" : "Jobs",
        "posts" : Job.objects.all(),
    }
    return render(request, "job-list.html", context)