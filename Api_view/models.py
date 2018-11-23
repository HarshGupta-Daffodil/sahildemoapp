# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class EmployeeDetail(models.Model):
    name = models.CharField(max_length=255)
    DOB = models.DateTimeField(auto_now_add=False)
    date_of_joining = models.DateTimeField(auto_now_add=True)
    experience = models.IntegerField(default=1)
    department = models.ForeignKey('Department', null=True, blank=True)
    skills = models.ManyToManyField('Skill')
    manager = models.ForeignKey('Manager', null=True, blank=True)


class Department(models.Model):
    name = models.CharField(max_length=255)
    manager = models.ForeignKey('Manager', null=True, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)


class Manager(models.Model):
    name = models.CharField(max_length=255)
    experience = models.IntegerField(default=1)
    DOB = models.DateTimeField(auto_now_add=False)
    date_of_joining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
