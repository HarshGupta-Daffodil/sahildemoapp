from rest_framework.serializers import ModelSerializer
from . models import *


class SkillDetailsSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class DeparmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'


