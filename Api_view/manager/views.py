from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Api_view.manager.models import *
from .serializer import MangerSerializer


class ManagerView(APIView):

    def get(self, request):
        """
        To list all the manager
        """
        manager = ManagerDetail.objects.all()
        response = {
            'details': MangerSerializer(
                manager,
                many=True
            ).data
        }
        return Response(response)

    def post(self, request):
        """
        Create a new entry
        """
        serializer = MangerSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(
                data='entry saved'
                )


class UpdateManager(APIView):

    def get(self, request, pk):
        """
        Reterive skill based on id
        """
        manager = ManagerDetail.objects.get(pk=pk)
        response = {
            'details': MangerSerializer(
                manager,
            ).data
        }
        return Response(response)

    def delete(self, request, pk):
        """
        Delete a particular entry based on id
        """
        manager = ManagerDetail.objects.get(pk=pk)
        manager.delete()
        return Response(
            data=' Entry deleted'
        )

    def put(self, request, pk):
        """
        update a particular entry based in id
        """
        manager = ManagerDetail.objects.get(pk=pk)
        serializer = MangerSerializer(manager, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'manager': manager})
        serializer.save()
        return Response(
            data='Entry Updated'
        )
