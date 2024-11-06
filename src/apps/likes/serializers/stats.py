from rest_framework import serializers

from apps.base.serializers.model_serializer import CustomModelSerializer


class DiscountLikesDislikesStatisticsSerializer(CustomModelSerializer):
    total_likes = serializers.IntegerField(read_only=True)
    total_dislikes = serializers.IntegerField(read_only=True)
    user_has_liked = serializers.BooleanField(read_only=True)
    user_has_disliked = serializers.BooleanField(read_only=True)

