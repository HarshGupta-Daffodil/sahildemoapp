from rest_framework.serializers import ModelSerializer
from .models import*


class SkillDetailsSerializer(ModelSerializer):
    class Meta:
        model = skill
        fields = '__all__'

