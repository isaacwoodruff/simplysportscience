from django.db import models
from django.utils import timezone

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
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    employer = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True,
                                        null=True,
                                        default=timezone.now)

    def __str__(self):
        return self.title + " - " + self.employer