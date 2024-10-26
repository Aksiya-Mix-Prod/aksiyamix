from apps.base.serializers.model_serializer import CustomModelSerializer
from apps.likes.models.likes import DiscountLike

class DiscountLikeSerializer(CustomModelSerializer):
    class Meta:
        model = DiscountLike
        fields = ['id', 'user', 'discount', 'created_at']
        read_only_fields = ['user', 'created_at']

