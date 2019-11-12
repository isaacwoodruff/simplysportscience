from django.shortcuts import render
from django.http import HttpResponse

def jobs_view(request):
    context = {"page_title": "Jobs"}
    return render(request, "jobs.html", context)