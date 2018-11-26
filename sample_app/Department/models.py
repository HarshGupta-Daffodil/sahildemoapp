# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..Manager.models import Manager


class Department(models.Model):
    name = models.CharField(max_length=255)
    manager = models.ForeignKey(Manager, null=True, blank=True)

