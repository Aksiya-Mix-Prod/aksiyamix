from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError

from src.apps.discounts.models import Discount
from src.apps.discounts.models import DiscountImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountImage
        fields = ['id', 'image']


class DiscountSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Discount
        fields = ['company', 'category', 'branch_company', 'tags', 'discount_type', 'currency', 'is_active',
                  'is_deleted', 'title', 'description', 'video_url', 'image', 'start_date', 'end_date', 'delivery',
                  'installment', 'discount_value', 'discount_value_is_percent', 'min_quantity', 'free_product',
                  'bonus_quantity', 'service',
                  ]
        read_only_fields = ['created_at',]

    def validate(self, data):
        discount_instance = Discount(**data)

        try:
            discount_instance.clean()
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        return data
