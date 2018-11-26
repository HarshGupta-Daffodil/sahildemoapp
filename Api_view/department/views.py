from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sample_app.serializers import DeparmentSerializer
from Api_view.department.models import Department
from Api_view.manager.models import Manager


class DepartmentView(APIView):

    def get(self, request):
        """
        To list all the Departments
        """
        departments = Department.objects.all()
        response = {
            'payment_methods': DeparmentSerializer(
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
        manager_id = request.data.pop('manager')
        manager = Manager.objects.get(pk=int(manager_id))
        Department.objects.update_or_create(manager=manager, **data)
        return Response(
                data=request.data
        )


class UpdateDepartment(APIView):

    def get(self, request, pk):
        """
        Reterive Department based on id
        """
        Departments = Department.objects.get(pk=pk)
        response = {
            'payment_methods': DeparmentSerializer(
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
        data = request.data
        manager_id = data.pop('manager')
        manager = Manager.objects.get(pk=manager_id)
        Department.objects.filter(pk=pk).update(manager=manager, **data)

        return Response(
            data='Entry Updated'
        )
