from apps.base.serializers import CustomModelSerializer
from apps.features.models import Feature
from apps.features.serializers.feature_values import FeatureValueListSerializer


class FeatureListSerializer(CustomModelSerializer):
    children = FeatureValueListSerializer(many=True)

    class Meta:
        model = Feature
        fields = (
            'category',
            'measure',
            'is_active',
            'ordering',
            'name',
            'children',
        )
