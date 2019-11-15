from django.contrib import admin
from .models import EmployerProfile, CandidateProfile

admin.site.register(EmployerProfile)
admin.site.register(CandidateProfile)