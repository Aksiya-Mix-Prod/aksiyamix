from apps.base.views import CustomCreateAPIView
from apps.services.serializers import ServiceCreateSerializer


class ServiceCreateAPIView(CustomCreateAPIView):
    serializer_class = ServiceCreateSerializer