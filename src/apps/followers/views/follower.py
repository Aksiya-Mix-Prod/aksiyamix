from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.base.views.viewsets import CustomModelViewSet
from apps.followers.models.follower import Follower
from apps.followers.serializers.follower import FollowerSerializer
from config.settings import REST_FRAMEWORK


class FollowerViewSet(CustomModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def my_followers(self, request):
        """
        Returns the list of followers for the authenticated user.
        """
        followers = self.get_queryset()
        serializer = FollowerSerializer(followers, many=True)
        return REST_FRAMEWORK(serializer.data, status=status.HTTP_200_OK)

    