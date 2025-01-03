from rest_framework.permissions import IsAuthenticated

from apps.base.views import CustomCreateAPIView
from apps.tops.permissions import IsCompanyOwner
from apps.tops.serializers import CreateTopDiscountSerializer
from apps.tops.models import TopDiscount


class CreateTopDiscountAPIView(CustomCreateAPIView):
    permission_classes = [IsAuthenticated, IsCompanyOwner]
    queryset = TopDiscount.objects.all()
    serializer_class = CreateTopDiscountSerializer