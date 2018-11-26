# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .models import Manager
from .serializer import MangerSerializer


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
