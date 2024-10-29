from apps.base.serializers.model_serializer import CustomModelSerializer
from apps.likes.models.dislikes import DiscountDislike

class DiscountDislikeSerializer(CustomModelSerializer):
    class Meta:
        model = DiscountDislike
        fields = ['id', 'user', 'discount', 'created_at']
        read_only_fields = ['user', 'created_at']

