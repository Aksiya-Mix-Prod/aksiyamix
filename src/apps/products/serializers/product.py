<<<<<<< HEAD
=======
from rest_framework import serializers

>>>>>>> 3b3e1be4f5f24ff0cf98aca5480a35c567612966
from apps.base.exceptions import CustomExceptionError
from apps.base.serializers import CustomModelSerializer
from apps.products.models import Product

<<<<<<< HEAD
class ProductSerializer(CustomModelSerializer):
=======

class ProductSerializer(serializers.ModelSerializer):
>>>>>>> 3b3e1be4f5f24ff0cf98aca5480a35c567612966
    class Meta:
        model = Product
        fields = ['id', 'company', 'category', 'title', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):
        company = attrs.get('company', None) or self.instance.company
        user = self.context['request'].user

        # Check user permissions
        if user != company.owner and not user.is_staff:
            raise CustomExceptionError(code=400, detail="You do not have permission to perform this action.")

        # Check the product count for the company
        product_count = Product.objects.filter(company=company).count()
        if product_count >= 10 and self.instance is None:
            raise CustomExceptionError(
                code=400,
                detail='Maximum number of products for this company reached. Please remove a product before adding a new one.'
            )

        return attrs

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user

        # Check user permissions
        if user != instance.company.owner and not user.is_staff:
            raise CustomExceptionError(code=400, detail="You do not have permission to perform this action.")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
