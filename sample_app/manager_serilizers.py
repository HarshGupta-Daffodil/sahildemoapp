from rest_framework.serializers import ModelSerializer
from . models import *


class MangerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'