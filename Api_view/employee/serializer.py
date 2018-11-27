from rest_framework.serializers import ModelSerializer
from Api_view.employee.models import *


class EmployeeDetailsSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
