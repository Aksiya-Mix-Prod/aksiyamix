from apps.base.serializers.model_serializer import CustomModelSerializer

from ..models.company import Company


class CompanyRatingSerializer(CustomModelSerializer):
    class Meta:
        model = Company
        fields = [
            "rating5",
            "rating4",
            "rating3",
            "rating2",
            "rating1",
            "rating_counts",
        ]
