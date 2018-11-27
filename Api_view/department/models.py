# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..manager.models import ManagerDetail


class DepartmentDetails(models.Model):
    name = models.CharField(max_length=255)
    manager = models.ForeignKey(ManagerDetail, null=True, blank=True)
