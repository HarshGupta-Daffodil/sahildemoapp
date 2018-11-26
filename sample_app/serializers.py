from rest_framework.serializers import ModelSerializer
from Api_view.department.models import *
from Api_view.skill.models import*
from Api_view.employee.models import *


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


