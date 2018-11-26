# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .models import *
from .serializer import DepartmentSerializer


class DepartmentList(generics.ListCreateAPIView):
    """
    list all departments of organisation
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class GetDepartment(generics.RetrieveAPIView):
    """
    Retrive a particular department by its id
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DeleteDepartment(generics.DestroyAPIView):
    """
    Delete a particular department by its id
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class UpdateDepartment(generics.UpdateAPIView):
    """
    Update a particular department by its id
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CreateDepartment(generics.ListCreateAPIView):
    """
    Create a new department with new id
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
