# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EmployeeDetail)
admin.site.register(Department)
admin.site.register(Skill)
admin.site.register(Manager)

