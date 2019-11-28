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
    VOLUNTEER = 'Volunteer'
    EMPLOYMENT_TYPE_CHOICES = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (CONTRACT, 'Contract'),
        (INTERNSHIP, 'Internship'),
        (APPRENTICESHIP, 'Apprenticeship'),
        (VOLUNTEER, 'Volunteer'),
    )

    employment_type = models.CharField(max_length=50,
                                       choices=EMPLOYMENT_TYPE_CHOICES,
                                       default=FULL_TIME)

    employer_fk = models.ForeignKey(
        EmployerProfile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    employer = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True,
                                          null=True,
                                          default=timezone.now)

    slug = models.SlugField(blank=True, null=True)

    class Meta:
        '''
        Ordering is set by the date created descending to give the newest results
        '''
        ordering = ['-created_date']

    def __str__(self):
        return self.title + " - " + self.employer

    def days_since_creation(self):
        '''
        Gets the amount of days ago that the post was created
        '''
        current_time = datetime.now()
        if self.created_date.month == current_time.month:
            days_since = str(current_time.day - self.created_date.day)

            if days_since == 0 or days_since == "0":
                return "Posted Today"
            else:
                return days_since + " days ago"
        return self.created_date.strftime("%b %d")

    def get_absolute_url(self):
        '''
        Generates the url for the job post with its slug
        '''
        return reverse('job_details', kwargs={'pk': self.pk, 'slug': self.slug})
