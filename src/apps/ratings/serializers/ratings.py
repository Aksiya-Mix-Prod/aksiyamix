from apps.base.serializers import CustomModelSerializer
from apps.ratings.models import Rating


class RatingSerializer(CustomModelSerializer):
    class Meta:
        model = Rating
        fields = ('company', 'rating_value')