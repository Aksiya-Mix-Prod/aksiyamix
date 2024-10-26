from apps.base.serializers import CustomModelSerializer
from apps.services.models import Service


class ServiceCreateSerializer(CustomModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name"]