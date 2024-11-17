from apps.base.serializers.model_serializer import CustomModelSerializer
from apps.notifications.models.notifications import Notification


class NotificationSerializer(CustomModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "notification_type",
            "company",
            "title",
            "image",
            "message",
        ]
