from django.shortcuts import render
from django.http import HttpResponse

def search_view(request):
    return HttpResponse("<h1>Search jobs</h1>")