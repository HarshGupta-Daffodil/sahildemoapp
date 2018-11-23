# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sample_app.models import *
from sample_app.serializers import DeparmentSerializer
from rest_framework import generics


class DepartmentList(generics.ListCreateAPIView):
    """
    list all departments of organisation
    """
    queryset = Department.objects.all()
    serializer_class = DeparmentSerializer


class GetDepartment(generics.RetrieveAPIView):
    """
    Retrive a particular department by its id
    """
    queryset = Department.objects.all()
    serializer_class = DeparmentSerializer


class DeleteDepartment(generics.DestroyAPIView):
    """
    Delete a particular department by its id
    """
    queryset = Department.objects.all()
    serializer_class = DeparmentSerializer


class UpdateDepartment(generics.UpdateAPIView):
    """
    Update a particular department by its id
    """
    queryset = Department.objects.all()
    serializer_class = DeparmentSerializer


class CreateDepartment(generics.ListCreateAPIView):
    """
    Create a new department with new id
    """
    queryset = Department.objects.all()
    serializer_class = DeparmentSerializer
