from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.base.views import CustomGenericAPIView
from apps.tops.models.company_top_tariff import CompanyTopTariff
from apps.tops.permissions import IsCompanyOwner
from apps.tops.serializers import BuyTopTariffSerializer


class BuyTopTariffGenericAPIView(CustomGenericAPIView):
    permission_classes = [IsAuthenticated, IsCompanyOwner]
    
    queryset = CompanyTopTariff.objects.none()
    serializer_class = BuyTopTariffSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)