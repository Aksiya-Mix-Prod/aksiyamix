from apps.base.serializers import CustomModelSerializer
from apps.services.models.services import Service


class ServiceListSerializer(CustomModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "icon"]