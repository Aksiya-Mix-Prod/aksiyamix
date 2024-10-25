from apps.base.serializers import CustomModelSerializer
from apps.discounts.models import DiscountFeature


class DiscountFeatureReceiveSerializer(CustomModelSerializer):
    class Meta:
        model = DiscountFeature
        fields = ['feature_value', 'price', 'old_price', 'quantity', 'remainder', ]
