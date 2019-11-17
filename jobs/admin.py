from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('pk', 'employer', 'title', 'location', 'employment_type', 'created_date', 'published_date',)

admin.site.register(Job, JobAdmin)
