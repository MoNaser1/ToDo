from django.db import models
from django.conf import settings


class Do(models.Model):
    title = models.CharField(max_length=50)
    creator = models.CharField(max_length=20)
    done = models.BooleanField(blank=False, null=True)
    description = models.TextField()
