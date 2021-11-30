from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField('Opublikowano')

