from rest_framework.serializers import ModelSerializer
from Api_view.manager.models import *


class MangerSerializer(ModelSerializer):
    class Meta:
        model = ManagerDetail
        fields = '__all__'