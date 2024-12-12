from rest_framework import serializers 

from apps.base.exceptions import CustomAPIExceptionError
from apps.base.serializers import CustomSerializer
from apps.companies.models.company import Company
from apps.tops.models import CompanyTopTariff
from apps.tops.models.top_tariff import TopTariff


class BuyTopTariffSerializer(CustomSerializer):
    top_tariff = serializers.PrimaryKeyRelatedField(queryset=TopTariff.objects.all())
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
     
    def validate(self, attrs):
        if attrs['company'].owner != attrs['user']:
            raise CustomAPIExceptionError(code=403, detail="You are not owner of this company")
        return super().validate(attrs)
    
    def create(self, validated_data):
        CompanyTopTariff.objects.create(company=validated_data['company'], quantity=validated_data['top_tariff'].quantity, price=validated_data['top_tariff'].price)
        return validated_data