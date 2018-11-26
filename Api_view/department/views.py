from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serilizer import DepartmentSerializer
from Api_view.department.models import Department
from Api_view.manager.models import Manager


class DepartmentView(APIView):

    def get(self, request):
        """
        To list all the Departments
        """
        departments = Department.objects.all()
        response = {
            'payment_methods':DepartmentSerializer(
                departments,
                many=True
            ).data
        }
        return Response(response)

    def post(self, request):
        """
        Create a new entry
        """
        data = request.data
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
        return Response(
                data="entry saved"
                )


class UpdateDepartment(APIView):

    def get(self, request, pk):
        """
        Reterive Department based on id
        """
        Departments = Department.objects.get(pk=pk)
        response = {
            'department':DepartmentSerializer(
                Departments,
            ).data
        }
        return Response(response)

    def delete(self, request, pk):
        """
        Delete a particular entry based on id
        """
        Departments = Department.objects.get(pk=pk)
        Departments.delete()
        return Response(
            data=' Entry deleted',
                   )

    def put(self, request, pk):
        """
        update a particular entry based in id
        """
        Departments = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(Departments, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(
            data='Entry Updated'
        )
