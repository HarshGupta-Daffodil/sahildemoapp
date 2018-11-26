from rest_framework.serializers import ModelSerializer
from .models import*


class SkillDetailsSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

