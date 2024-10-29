from rest_framework.permissions import IsAuthenticated

from apps.appeals.models import Appeal
from apps.appeals.serializers.appeals import AppealSerializer
from apps.base.views import CustomModelViewSet


class AppealCreateViewSet(CustomModelViewSet):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
