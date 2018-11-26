from __future__ import unicode_literals

from django.db import models


class Manager(models.Model):
    name = models.CharField(max_length=255)
    experience = models.IntegerField(default=1)
    dob = models.DateTimeField(auto_now_add=False)
    date_of_joining = models.DateTimeField(auto_now_add=True)

  