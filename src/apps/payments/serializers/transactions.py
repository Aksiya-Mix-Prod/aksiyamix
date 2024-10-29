from apps.payments.models import Transaction
from apps.base.serializers import CustomModelSerializer


class TransactionSerializer(CustomModelSerializer):
    """
    Transaction serializer class
    """
    class Meta:
        model = Transaction
        fields = ['order', 'payment_system', 'date_time', 'status', 'error_message', 'amount']