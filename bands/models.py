from __future__ import unicode_literals

from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
