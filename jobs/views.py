from django.shortcuts import render
from django.http import HttpResponse

job_posts = [
    {
        "title" : "performance analyst",
        "description" : "Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum",
        "location" : "galway, ireland",
        "employer" : "pied piper",
        "employment_type" : "full time",
        "date_created" : "1d"
    },
    {
        "title" : "performance analyst",
        "description" : "Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum",
        "location" : "galway, ireland",
        "employer" : "pied piper",
        "employment_type" : "full time",
        "date_created" : "1d"
    },
    {
        "title" : "performance analyst",
        "description" : "Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum",
        "location" : "galway, ireland",
        "employer" : "pied piper",
        "employment_type" : "full time",
        "date_created" : "1d"
    },
    {
        "title" : "performance analyst",
        "description" : "Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum",
        "location" : "galway, ireland",
        "employer" : "pied piper",
        "employment_type" : "full time",
        "date_created" : "1d"
    }
]

def jobs_view(request):
    context = {
        "page_title" : "Jobs",
        "posts" : job_posts,
    }
    return render(request, "jobs.html", context)