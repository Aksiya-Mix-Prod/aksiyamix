from apps.advertisements.models.advertisement import Advertisement
from apps.advertisements.serializers.advertisement import AdvertisementSerializer
from apps.base.views.viewsets import CustomModelViewSet
from django.utils import timezone
from rest_framework.permissions import IsAdminUser


class AdvertisementViewSet(CustomModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        """To get active ads only from ads that collide with the current date"""
        return Advertisement.objects.filter(
            is_active=True,
            payment_status=Advertisement.PaymentStatusChoices.PAID,
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now(),
        ).order_by("ordering")
