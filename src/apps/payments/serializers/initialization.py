from django.conf import settings
from apps.payments.models import Order
from rest_framework import serializers
from apps.base.serializers import  CustomModelSerializer



class PaymentInitSerializer(CustomModelSerializer):
    payme_data = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['_id', 'amount', 'payme_data']

    def get_payme_data(self, obj):
        return {
            'merchant': settings.PAYME_PASSWORD,
            # ========  Convert to tiyin ========
            'amount': int(obj.amount * 100),
            'account': {
                'order_id': obj._id
            },
            'description': f'Payment for order {obj._id}'
        }