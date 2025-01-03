from apps.base.serializers import CustomModelSerializer
from apps.tops.models import TopDiscount
from apps.discounts.serializers import DiscountCreateUpdateSerializer


class TopListSerializer(CustomModelSerializer):
    discount = DiscountCreateUpdateSerializer(read_only=True)
    
    class Meta:
        model = TopDiscount
        fields = ('id', 'discount')