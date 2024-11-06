from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from apps.base.views import CustomRetrieveUpdateAPIView
from apps.users.serializers import UserProfileRetrieveUpdateModelSerializer


class UserProfileRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserProfileRetrieveUpdateModelSerializer

    def get_object(self):
        return self.request.user