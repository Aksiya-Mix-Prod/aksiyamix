from django.utils.timezone import now
from django.db.models.query import QuerySet

from apps.base.views import CustomListAPIView
from apps.tops.models import TopDiscount
from apps.tops.serializers import TopListSerializer


class TopListAPIView(CustomListAPIView):
    serializer_class = TopListSerializer
    queryset = TopDiscount.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        result = []
        for obj in queryset:
            for date in obj.dates:
                if date == now().date():
                    if not obj in result:
                        result.append(obj)
        return queryset.filter(id__in=[obj.id for obj in result])