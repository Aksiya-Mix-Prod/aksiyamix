from apps.base.serializers import CustomModelSerializer
from apps.features.models import FeatureValue


class FeatureValueListSerializer(CustomModelSerializer):
    class Meta:
        model = FeatureValue
        fields = (
            'feature',
            'value',
            'slug',
            'is_active',
            'ordering',
        )