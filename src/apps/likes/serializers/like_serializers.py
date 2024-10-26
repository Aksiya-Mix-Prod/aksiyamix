from rest_framework import serializers
from apps.base.serializers.model_serializer import CustomModelSerializer
from apps.likes.models.likes import DiscountLike

class DiscountLikeSerializer(CustomModelSerializer):
    class Meta:


