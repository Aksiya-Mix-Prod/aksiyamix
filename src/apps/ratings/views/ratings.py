from rest_framework.permissions import IsAuthenticated

from apps.base.views import CustomModelViewSet
from apps.ratings.models import Rating
from apps.ratings.serializers import RatingSerializer


class RatingCreateViewSet(CustomModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

