# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .models import *
from .serializer import EmployeeDetailsSerializer


class EmployeeList(generics.ListCreateAPIView):
    """
    Generic view to show the list of all employee
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeDetailsSerializer


class GetEmployee(generics.RetrieveAPIView):
    """
    Retrive a particular employee by its id
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeDetailsSerializer


class DeleteEmployee(generics.DestroyAPIView):
    """
    Delete a particular employee by its id
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeDetailsSerializer


class UpdateEmployee(generics.UpdateAPIView):
    """
    Update a particular employee by its id
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeDetailsSerializer


class CreateEmployee(generics.ListCreateAPIView):
    """
    Create new Employee
    """
    queryset = EmployeeDetail.objects
    serializer_class = EmployeeDetailsSerializer
