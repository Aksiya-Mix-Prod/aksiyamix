from rest_framework import serializers
from django.utils.text import slugify
from src.apps.discounts.models.servicediscount import ServiceDiscount


class ServiceDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDiscount
        fields = ['id', 'name', 'slug', 'icon', 'is_active']
        read_only_fields = ['slug']

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data.get('name', ''))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'name' in validated_data:
            validated_data['slug'] = slugify(validated_data.get('name', ''))
        return super().update(instance, validated_data)
