from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import EmployerProfile


class Job(models.Model):
    """
    A single Job post
    """
    FULL_TIME = 'Full Time'
    PART_TIME = 'Part Time'
    CONTRACT = 'Contract'
    INTERNSHIP = 'Internship'
    APPRENTICESHIP = 'Apprenticeship'
    EMPLOYMENT_TYPE_CHOICES = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (CONTRACT, 'Contract'),
        (INTERNSHIP, 'Internship'),
        (APPRENTICESHIP, 'Apprenticeship'),
    )

    employment_type = models.CharField(max_length=50,
                                        choices=EMPLOYMENT_TYPE_CHOICES,
                                        default=FULL_TIME)

    employer_fk = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    requirements = models.TextField(default="")
    location = models.CharField(max_length=100)
    employer = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True,
                                          null=True,
                                          default=timezone.now)

    slug = models.SlugField(default="")

    def __str__(self):
        return self.title + " - " + self.employer

    def get_absolute_url(self):
        return reverse('job_details', kwargs={'pk': self.pk, 'slug': self.slug})
