from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Api_view.employee.models import *
from Api_view.department.models import *
from Api_view.manager.models import *
from Api_view.skill.models import *
from .serializer import EmployeeDetailsSerializer


class EmployeeView(APIView):

    def get(self, request):
        """
        To list all the employee
        """
        employee = EmployeeDetail.objects.all()
        response = {
            'details': EmployeeDetailsSerializer(
                employee,
                many=True
            ).data
        }
        return Response(response)

    def post(self, request):
        """
        Create a new entry
        """
        data = request.data
        serializer = EmployeeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
        return Response(
                data="entry saved"
                )


class UpdateEployee(APIView):
    def get(self, request, pk):
        """
        Reterive EmployeeDetail based on id
        """
        employee = EmployeeDetail.objects.get(pk=pk)
        response = {
            'details': EmployeeDetailsSerializer(
                employee,
            ).data
        }
        return Response(response)

    def delete(self, request, pk):
        """
        Delete a particular entry based on id
        """
        employee = EmployeeDetail.objects.get(pk=pk)
        employee.delete()
        return Response(
            data=' Entry deleted'
        )

    def put(self, request, pk):
        """
        update a particular entry based in id
        """
        employee = EmployeeDetail.objects.get(pk=pk)
        serializer = EmployeeDetailsSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(
                data="request.data"
                )