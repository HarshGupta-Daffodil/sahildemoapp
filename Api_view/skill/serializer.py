from rest_framework.serializers import ModelSerializer
from Api_view.skill.models import*


class SkillDetailsSerializer(ModelSerializer):
    class Meta:
        model = SkillDetails
        fields = '__all__'

