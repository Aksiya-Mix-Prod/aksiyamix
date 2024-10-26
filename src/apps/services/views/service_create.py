from rest_framework.permissions import IsAuthenticated

from apps.base.views import CustomCreateAPIView
from apps.services.serializers import ServiceCreateSerializer


class ServiceCreateAPIView(CustomCreateAPIView):
    """
    Create a new service
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceCreateSerializer