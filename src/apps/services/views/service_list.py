from apps.base.views import CustomListAPIView
from apps.services.models.services import Service
from apps.services.serializers.service_list import ServiceListSerializer


class ServiceListAPIView(CustomListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceListSerializer
