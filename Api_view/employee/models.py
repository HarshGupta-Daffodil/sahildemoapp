from __future__ import unicode_literals

from django.db import models
from ..manager.models import ManagerDetail
from ..skill.models import SkillDetails
from ..department.models import DepartmentDetails


class Employee(models.Model):
    name = models.CharField(max_length=255)
    DOB = models.DateTimeField(auto_now_add=False)
    date_of_joining = models.DateTimeField(auto_now_add=True)
    experience = models.IntegerField(default=1)
    department = models.ForeignKey(DepartmentDetails, null=True, blank=True)
    skills = models.ManyToManyField(SkillDetails)
    manager = models.ForeignKey(ManagerDetail, null=True, blank=True)
