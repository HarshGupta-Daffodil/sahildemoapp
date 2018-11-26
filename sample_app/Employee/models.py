from __future__ import unicode_literals

from django.db import models
from ..Manager.models import Manager
from ..Skill.models import Skill
from ..Department.models import Department


class EmployeeDetail(models.Model):
    name = models.CharField(max_length=255)
    DOB = models.DateTimeField(auto_now_add=False)
    date_of_joining = models.DateTimeField(auto_now_add=True)
    experience = models.IntegerField(default=1)
    department = models.ForeignKey(Department, null=True, blank=True)
    skills = models.ManyToManyField(Skill)
    manager = models.ForeignKey(Manager, null=True, blank=True)
