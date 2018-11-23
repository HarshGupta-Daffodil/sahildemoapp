# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sample_app.models import EmployeeDetail, Manager, Skill
from sample_app.manager_serilizers import MangerSerializer
from rest_framework import generics


class ManagerList(generics.ListCreateAPIView):
    """
    list all Managers
    """
    queryset = Manager.objects.all()
    serializer_class = MangerSerializer


class GetManager(generics.RetrieveAPIView):
    """
    Retrive a particular Manager by its id
    """
    queryset = Manager.objects.all()
    serializer_class = MangerSerializer


class DeleteManager(generics.DestroyAPIView):
    """
    Delete a particular Manager by its id
    """
    queryset = Manager.objects.all()
    serializer_class = MangerSerializer


class UpdateManager(generics.UpdateAPIView):
    """
    Update a particular Manager by its id
    """
    queryset = Manager.objects.all()
    serializer_class = MangerSerializer


class CreateManager(generics.ListCreateAPIView):
    """
    Create a new Manager
    """
    queryset = Manager.objects.all()
    serializer_class = MangerSerializer
