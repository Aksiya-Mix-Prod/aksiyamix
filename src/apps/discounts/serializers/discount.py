from django.db import transaction
from apps.base.exceptions import CustomExceptionError
from apps.base.serializers import CustomModelSerializer
from apps.discounts.models import Discount, DiscountFeature, DiscountImage
from apps.discounts.serializers.discount_feature import DiscountFeatureReceiveSerializer


class ProductImageSerializer(CustomModelSerializer):
    class Meta:
        model = DiscountImage
        fields = ['id', 'image']


class DiscountCreateUpdateSerializer(CustomModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    features = DiscountFeatureReceiveSerializer(many=True, write_only=True)

    class Meta:
        model = Discount
        fields = [
            'id', 'features', 'company', 'category', 'branch_company', 'tags', 'discount_type', 'currency',
            'is_active', 'is_deleted', 'title', 'description', 'video_url', 'image', 'start_date', 'end_date',
            'delivery', 'installment', 'discount_value', 'discount_value_is_percent', 'min_quantity', 'free_product',
            'bonus_quantity', 'service'
        ]
        read_only_fields = ['created_at']

    def validate(self, data):
        discount_instance = Discount(**data)
        try:
            discount_instance.clean()
        except Exception as e:
            raise CustomExceptionError(code=400, detail=str(e))
        return data

    @transaction.atomic
    def create(self, validated_data):
        user = self.context['request'].user
        company = validated_data.get('company')

        # Check user permissions
        if user != company.owner and not user.is_staff:
            raise CustomExceptionError(code=400, detail="You do not have permission to perform this action.")

        features_data = validated_data.pop('features', [])
        discount = super().create(validated_data)

        if features_data:
            DiscountFeature.objects.bulk_create([
                DiscountFeature(discount=discount, **feature)
                for feature in features_data
            ])

        return discount

    @transaction.atomic
    def update(self, instance, validated_data):
        user = self.context['request'].user
        company = validated_data.get(
            'company') or instance.company  # Get company from validated data or existing instance

        # Check user permissions
        if user != company.owner and not user.is_staff:
            raise CustomExceptionError(code=400, detail="You do not have permission to perform this action.")

        features_data = validated_data.pop('features', [])
        discount = super().update(instance, validated_data)

        if features_data:
            DiscountFeature.objects.filter(discount_id=discount.pk).delete()
            DiscountFeature.objects.bulk_create([
                DiscountFeature(discount_id=discount.pk, **feature)
                for feature in features_data
            ])

        return discount
