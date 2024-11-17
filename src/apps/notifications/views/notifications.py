from django.utils.translation import gettext_lazy as _
from fcm_django.models import FCMDevice
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.base.views.viewsets import CustomModelViewSet
from apps.notifications.models.notifications import Notification
from apps.notifications.serializers.notifications import NotificationSerializer


class NotificationViewSet(CustomModelViewSet):
    queryset = Notification
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Create Notification and send to user."""

        notification = serializer.save()

        user = self.request.user

        filters = {
            Notification.Type.LOGIN: FCMDevice.objects.filter(user=user),
            Notification.Type.NEWS: FCMDevice.objects.filter(user__is_active=True),
            Notification.Type.FOLLOW: FCMDevice.objects.filter(user=notification.user),
            Notification.Type.DISCOUNT: FCMDevice.objects.filter(
                user__in=notification.company.followers.all()
            ),
            Notification.Type.COMMENT: FCMDevice.objects.filter(
                user__in=notification.related_post.followers.all()
            ),  # last
            Notification.Type.COMPLAINT: FCMDevice.objects.filter(
                user__company=notification.company
            ),
            Notification.Type.SPAM: FCMDevice.objects.filter(
                user__is_active=True
            ),  # last
            Notification.Type.PAYMENT: FCMDevice.objects.filter(
                user__has_made_payment=True
            ),
            Notification.Type.ADVERTISING: FCMDevice.objects.filter(
                user__is_active=True
            ),
        }

        devices = filters.get(notification.notification_type, FCMDevice.objects.none())

        icon_url = notification.image.url if notification.image else None

        try:
            devices.send_message(
                title=_(notification.title),
                message=_(notification.message),
                icon=icon_url,
            )
        except Exception as e:
            print(f"Error sending notification: {e}")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def register_device(self, request):
        token = request.data.get('token')
        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

        device, created = FCMDevice.objects.get_or_create(
            registration_id=token, user=request.user, type="web"
        )
        if created:
            return Response({"message": "Device registered successfully."}, status=status.HTTP_201_CREATED)
        return Response({"message": "Device already registered."}, status=status.HTTP_200_OK)
