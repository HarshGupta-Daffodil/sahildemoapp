from rest_framework.serializers import ModelSerializer
from Api_view.employee.models import *


class EmployeeDetailsSerializer(ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'
