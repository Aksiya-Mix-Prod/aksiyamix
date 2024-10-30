from rest_framework import serializers

from apps.base.serializers.model_serializer import CustomModelSerializer
from apps.companies.models import Company
from apps.followers.models.follower import Follower


class FollowerSerializer(CustomModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    company_ids = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(),
                                                     many=True, write_only=True)
    companies = serializers.PrimaryKeyRelatedField(source='company', many=True, read_only=True)

    class Meta:
        model = Follower
        fields = [
            'user', 'company_ids', 'companies'
        ]

    def create(self, validate_data):
        user = self.context['request'].user
        company_ids = validate_data.pop('company_ids', [])
        follower = Follower.objects.all(user=user)

        #Add companies to the follower
        follower.company.set(company_ids)
        return follower
