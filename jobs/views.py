from django.shortcuts import render
from django.http import HttpResponse

def jobs_view(request):
    return HttpResponse("<h1>Jobs</h1>")