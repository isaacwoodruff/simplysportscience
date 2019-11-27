from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


'''
The EmployerProfile model has a slug field which is used in the search app along with the
primary key for the url that displays all the jobs from the employer
'''
class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=True)
    is_candidate = models.BooleanField(default=False)
    company_name = models.CharField(max_length=200)

    slug = models.SlugField(default="")

    def __str__(self):
        return f"{self.company_name} Profile"

    def get_absolute_url(self):
        return reverse('employer_job_list', kwargs={'pk': self.pk, 'slug': self.slug})


class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_candidate = models.BooleanField(default=True)
    is_employer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} Profile"


'''
When a User object is created or updated this receiver function creates or updates
a user (employer or candidate) profile object
'''
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if instance.first_name != "":
        if created:
            CandidateProfile.objects.create(user=instance)
        instance.candidateprofile.save()
    else:
        if created:
            EmployerProfile.objects.create(user=instance)
        instance.employerprofile.save()
