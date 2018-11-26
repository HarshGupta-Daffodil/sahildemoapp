from rest_framework.serializers import ModelSerializer
from Api_view.department.models import *


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

