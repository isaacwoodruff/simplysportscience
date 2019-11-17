from django.contrib import admin
from .models import EmployerProfile, CandidateProfile

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'company_name', 'is_employer', 'is_candidate', 'user',)

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'is_employer', 'is_candidate', 'user',)

admin.site.register(EmployerProfile, EmployerAdmin)
admin.site.register(CandidateProfile, CandidateAdmin)
