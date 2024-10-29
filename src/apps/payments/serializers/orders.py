from apps.payments.models import Order
from apps.base.serializers import CustomModelSerializer


class OrderSerializer(CustomModelSerializer):
    """
    Serializer for the Order model
    """
    class Meta:
        model = Order
        fields = ['_id', 'company', 'amount', 'is_paid']
        read_only_fields = ['is_paid']

