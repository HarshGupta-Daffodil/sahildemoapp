from rest_framework.serializers import ModelSerializer
from .models import *


class EmployeeDetailsSerializer(ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'
