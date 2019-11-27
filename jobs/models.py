from datetime import datetime
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

    employer_fk = models.ForeignKey(
        EmployerProfile, on_delete=models.CASCADE, null=True)
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

    '''Ordering is set by the date created descending to give the newest results'''
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title + " - " + self.employer

    '''Gets the amount of days ago that the post was created'''
    def days_since_creation(self):
        current_time = datetime.now()
        if self.created_date.month == current_time.month:
            days_since = str(current_time.day - self.created_date.day)

            if days_since == 0 or days_since == "0":
                return "Posted Today"
            else:
                return  days_since + " days ago"
        return self.created_date.strftime("%b %d")

    '''Generates the url for the job post with its slug'''
    def get_absolute_url(self):
        return reverse('job_details', kwargs={'pk': self.pk, 'slug': self.slug})
