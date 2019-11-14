from django.db import models
from django.utils import timezone

class Job(models.Model):
    """
    A single Job post
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    employer = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " - " + self.employer