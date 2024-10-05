from rest_framework import serializers

from .discountimage import DiscountImageSerializer
from src.apps.discounts.models import Discount
from src.apps.discounts.choices import DiscountChoices
from src.apps.discounts.models import DiscountImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountImage
        fields = ['id', 'image']

class DiscountSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Discount
        fields = [
            'company', 'branch_company', 'category', 'status', 'discount_type',
            'currency', 'title', 'old_price', 'description', 'video', 'id_generate',
            'in_stock', 'available', 'views', 'likes', 'dislikes', 'start_date',
            'end_date', 'delivery', 'installment', 'is_active', 'created_at',
            'ordering', 'discount_value', 'discount_value_is_percent', 'min_quantity',
            'bonus_quantity', 'bonus_discount_value', 'bonus_discount_value_is_percent',
            'service'
        ]
        read_only_fields = ['created_at', 'ordering']

    def validate_discount_value(self, value):
        if self.instance and self.instance.discount_value_is_percent and value:
            if not (0 <= value <= 100):
                raise serializers.ValidationError("Discount must be a percentage between 0 and 100")
        return value

    def validate(self, data):
        if data.get('discount_type') == DiscountChoices.STANDARD and data.get('discount_value') is None:
            raise serializers.ValidationError("Standard discount must have a discount_value")

        if data.get('discount_type') == DiscountChoices.FREE_PRODUCT:
            if not data.get('min_quantity') or not data.get('bonus_quantity'):
                raise serializers.ValidationError("Free product discount requires min_quantity and bonus_quantity")

        if data.get('discount_type') == DiscountChoices.QUANTITY_DISCOUNT:
            if not data.get('min_quantity') or not data.get('bonus_discount_value'):
                raise serializers.ValidationError("Quantity discount requires min_quantity and bonus_discount_value")

        if data.get('discount_type') == DiscountChoices.SERVICE_DISCOUNT:
            if not data.get('min_quantity') or not data.get('service'):
                raise serializers.ValidationError("Service discount requires min_quantity and a service")

        return data
