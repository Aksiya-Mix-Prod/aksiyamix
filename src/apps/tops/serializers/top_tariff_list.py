from apps.base.serializers import CustomModelSerializer
from apps.tops.models.top_tariff import TopTariff


class TopTariffListSerializer(CustomModelSerializer):
    class Meta:
        model = TopTariff
        fields = '__all__'