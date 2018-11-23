# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sample_app.models import *
from sample_app.serializers import EmployeeSerializer
from rest_framework import generics


class EmployeeList(generics.ListCreateAPIView):
    """
    Generic view to show the list of all employee
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeSerializer


class GetEmployee(generics.RetrieveAPIView):
    """
    Retrive a particular employee by its id
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeSerializer


class DeleteEmployee(generics.DestroyAPIView):
    """
    Delete a particular employee by its id
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeSerializer


class UpdateEmployee(generics.UpdateAPIView):
    """
    Update a particular employee by its id
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeSerializer


class CreateEmployee(generics.ListCreateAPIView):
    """
    Create new Employee
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeSerializer
