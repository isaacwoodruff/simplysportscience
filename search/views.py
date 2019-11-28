import os
import json
import operator
from functools import reduce
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Q
from jobs.models import Job, EmployerProfile
from django.core.paginator import Paginator


'''
Algolia keys are for Algolia API which is used to auto-suggest locations in the location search
'''
ALGOLIA_PUBLIC_KEY = os.environ.get('ALGOLIA_PUBLIC_KEY')
ALGOLIA_PUBLIC_APP_ID = os.environ.get('ALGOLIA_PUBLIC_APP_ID')


'''
Querys all the job posts and renders them paginated by 10 posts per page
'''
def job_list(request):
    job_posts = Job.objects.all()
    paginator = Paginator(job_posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "page_title": "Explore thousands of Jobs",
        "posts": posts,
        "ALGOLIA_PUBLIC_KEY": ALGOLIA_PUBLIC_KEY,
        "ALGOLIA_PUBLIC_APP_ID": ALGOLIA_PUBLIC_APP_ID,
    }
    return render(request, "job-list.html", context)


'''
Gets all employer jobs or 404 and renders them paginated by 10 posts per page
'''
def employer_job_list(request, pk, slug=""):
    employer_object = get_object_or_404(EmployerProfile, pk=pk)

    page_title = employer_object.company_name + " " + "Jobs"

    job_posts = Job.objects.filter(employer_fk=employer_object)
    paginator = Paginator(job_posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "page_title": page_title,
        "posts": posts,
        "ALGOLIA_PUBLIC_KEY": ALGOLIA_PUBLIC_KEY,
        "ALGOLIA_PUBLIC_APP_ID": ALGOLIA_PUBLIC_APP_ID,
    }
    return render(request, "job-list.html", context)


'''
Gets employment_type from GET request and querys all jobs with that employment_type
an renders them paginated by 10 posts per page
'''
def employment_type_job_list(request):
    employment_type = request.GET.get('type')
    page_title = employment_type + " Jobs"

    job_posts = Job.objects.filter(employment_type=employment_type)
    paginator = Paginator(job_posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "page_title": page_title,
        "posts": posts,
        "ALGOLIA_PUBLIC_KEY": ALGOLIA_PUBLIC_KEY,
        "ALGOLIA_PUBLIC_APP_ID": ALGOLIA_PUBLIC_APP_ID,
    }
    return render(request, "job-list.html", context)


'''
Gets location from GET request and querys all jobs with that location
an renders them paginated by 10 posts per page
'''
def location_job_list(request):
    location = request.GET['in']
    page_title = "Jobs in " + location

    job_posts = Job.objects.filter(location__icontains=location)
    paginator = Paginator(job_posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "page_title": page_title,
        "posts": posts,
        "ALGOLIA_PUBLIC_KEY": ALGOLIA_PUBLIC_KEY,
        "ALGOLIA_PUBLIC_APP_ID": ALGOLIA_PUBLIC_APP_ID,
    }
    return render(request, "job-list.html", context)


'''
Finds all jobs in database by what user is typing and sends json data to suggest
an autocomplete for job title search. The set() method removes duplicates.
'''
def autocomplete_title_search(request):
    if request.is_ajax():
        job_query = request.GET.get('term', '')
        titles = Job.objects.filter(
            Q(title__istartswith=job_query) | Q(title__icontains=job_query)
        ).distinct()
        result = []
        for title in titles:
            title_json = title.title
            result.append(title_json)
        unique_list = list(set(result))
        data = json.dumps(unique_list)
        mimetype = 'application/json'
    return HttpResponse(data, mimetype)


'''
Takes job-title, location, and employment_type from GET request.

Puts job-title and location into form_data to fill search bar fields with previous search.

Three if statements check to see if the search fields contain any values, if they do then
a query of that search value is appended onto the query_list.

If the query_list is empty then it searches the database for all jobs.
If the query_list is not empty a reduce method gets every value in the query_list
and adds a | (and) operator onto it. This inside the filter method, allows a dynamic/variable
search query to find jobs from the search bar fields.

These are then rendered and paginated by 10 posts per page.
'''
def search_results(request):
    job_query = request.GET.get('job-title')
    location_query = request.GET.get('location')
    employment_type_query = request.GET.getlist('employment-type')
    form_data = {
        "job_query": job_query,
        "location_query": location_query,
    }
    query_list = []

    if job_query is not None and job_query != "":
        query_list.append(Q(title__icontains=job_query))

    if location_query is not None and location_query != "":
        query_list.append(Q(location__icontains=location_query))

    if employment_type_query is not None and employment_type_query != []:
        query_list.append(Q(employment_type__in=employment_type_query))

    if query_list == [] or query_list is None:
        job_posts = Job.objects.all()
    else:
        job_posts = Job.objects.filter(
            reduce(operator.and_, (query for query in query_list)))

    paginator = Paginator(job_posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if location_query == "" or location_query is None:
        page_title = job_query.title() + " Jobs Anywhere"
    else:
        page_title = job_query.title() + " Jobs in " + location_query.title()

    context = {
        "page_title": page_title,
        "posts": posts,
        "form_data": form_data,
        "ALGOLIA_PUBLIC_KEY": ALGOLIA_PUBLIC_KEY,
        "ALGOLIA_PUBLIC_APP_ID": ALGOLIA_PUBLIC_APP_ID,
    }
    return render(request, "job-list.html", context)
