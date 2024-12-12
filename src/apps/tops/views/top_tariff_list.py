from apps.base.views import CustomListAPIView
from apps.tops.models import TopTariff
from apps.tops.serializers import TopTariffListSerializer


class TopTariffListAPIView(CustomListAPIView):
    queryset = TopTariff.objects.all()
    serializer_class = TopTariffListSerializer