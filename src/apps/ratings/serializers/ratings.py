from apps.base.serializers import CustomModelSerializer
from apps.ratings.models import Rating


class RatingSerializer(CustomModelSerializer):
    class Meta:
        model = Rating
        fields = ('company', 'rating_value')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
