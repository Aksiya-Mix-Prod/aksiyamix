from rest_framework import serializers
from apps.products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['company', 'name', 'image']

    def validate(self, attrs):
        company = attrs.get('company')
        product_count = Product.objects.filter(company=company).count()

        if product_count >= 10:
            raise serializers.ValidationError(
                {"company": "This company already has 4 products. No more products can be added."}
            )

        return attrs
