from rest_framework.serializers import ModelSerializer

from Api_view.department.models import *


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = DepartmentDetails
        fields = '__all__'

