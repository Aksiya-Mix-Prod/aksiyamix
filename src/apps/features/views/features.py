from rest_framework.permissions import IsAuthenticated

from apps.base.views import CustomListAPIView
from apps.features.models import Feature
from apps.features.serializers import FeatureListSerializer


class FeatureListListAPIView(CustomListAPIView):
    """ feature list view """

    permission_classes = (IsAuthenticated,)
    queryset = Feature.obejcts.filter(is_active=True).prefetch_related('children').order_by('ordering')
    serializer_class = FeatureListSerializer

