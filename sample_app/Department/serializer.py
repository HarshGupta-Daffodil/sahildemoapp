from rest_framework.serializers import ModelSerializer
from .models import *


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
