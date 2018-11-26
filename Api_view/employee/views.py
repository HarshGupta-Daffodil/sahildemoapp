from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sample_app.serializers import EmployeeSerializer
from Api_view.employee.models import *
from Api_view.department.models import *
from Api_view.manager.models import *
from Api_view.skill.models import *


class EmployeeView(APIView):

    def get(self, request):
        """
        To list all the employee
        """
        employee = EmployeeDetail.objects.all()
        response = {
            'payment_methods': EmployeeSerializer(
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
        skill_data = data.pop('skills')
        Department_name = data.pop('department')
        department = Department.objects.get(name=Department_name)
        manager_name = data.pop('manager')
        manager = Manager.objects.get(name=manager_name)
        Employee = EmployeeDetail.objects.create(department=department, manager=manager, **data)
        Employee.save()
        for skill in skill_data:
            skill_add, create = Skill.objects.get_or_create(name=skill)
            Employee.skills.add(skill_add)
        return Response(
                data=request.data
                )


class UpdateEployee(APIView):
    def get(self, request, pk):
        """
        Reterive EmployeeDetail based on id
        """
        employee = EmployeeDetail.objects.get(pk=pk)
        response = {
            'payment_methods': EmployeeSerializer(
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
            data=' Entry deleted',
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk):
        """
        update a particular entry based in id
        """
        data = request.data
        data.pop('skills')
        Department_name = data.pop('department')
        department = Department.objects.get(name=Department_name)
        manager_name = data.pop('manager')
        manager = Manager.objects.get(name=manager_name)
        EmployeeDetail.objects.filter(pk=pk).update(department=department, manager=manager, **data)
        return Response(
                data="request.data"
                )