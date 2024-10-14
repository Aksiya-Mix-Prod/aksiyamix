from rest_framework import serializers
from src.apps.discounts.models import DiscountImage



class DiscountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountImage
        fields = ['discount', 'image', 'ordering_number', 'created_at']
        read_only_fields = ['created_at']
