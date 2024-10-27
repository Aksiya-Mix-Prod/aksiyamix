from django.db.models import QuerySet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.packets.models import Packet
from apps.base.views import CustomGenericViewSet
from apps.packets.permissions.permissions import IsAdminOrIsCompanyOwner
from apps.packets.serializers.packets import PacketSerializer


class PacketGenericViewSet(CustomGenericViewSet):
    """
    ViewSet for listing Packet
    """
    permission_classes = [IsAuthenticated, IsAdminOrIsCompanyOwner]
    serializer_class = PacketSerializer

    def get_queryset(self) -> QuerySet:
        """
        Override this to return a list of all Packet objects
        """
        if self.action == 'list':
            return Packet.objects.all().order_by('-created_at')
        else:
            return Packet.objects.none()


    @action(detail=False, methods=['GET'], url_path='list-all-packets')
    def list_packets(self, request) -> Response:
        """
        List all packets available for a company:
        - Ordered by most recently created date
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


