from rest_framework import serializers

from apps.base.exceptions import CustomExceptionError
from apps.base.serializers import CustomModelSerializer
from apps.branches.models.branch import BranchCompany


class BranchListSerializer(CustomModelSerializer):
    company = serializers.StringRelatedField()
    region_display = serializers.CharField(source='get_region_display', read_only=True)
    district_display = serializers.CharField(source='get_district_display', read_only=True)

    class Meta:
        model = BranchCompany
        fields = [
            'id_branch',
            'company',
            'title',
            'phone_number1',
            'phone_number2',
            'address',
            'region',
            'region_display',
            'district',
            'district_display',
            'delivery',
            'longitude',
            'latitude',
        ]
        read_only_fields = ['id_branch']


class BranchDetailSerializer(CustomModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = BranchCompany
        fields = [
            'id_branch',
            'company',
            'title',
            'phone_number1',
            'phone_number2',
            'address',
            'region',
            'region_display',
            'district',
            'district_display',
            'delivery',
            'longitude',
            'latitude',
        ]
        read_only_fields = ['id_branch']


class BranchCreateSerializer(CustomModelSerializer):
    class Meta:
        model = BranchCompany
        fields = [
            'company',
            'title',
            'phone_number1',
            'phone_number2',
            'address',
            'region',
            'district',
            'delivery',
            'longitude',
            'latitude',
        ]

        def create(self, validate_data):
            branch = BranchCompany.objects.create(**validate_data)
            branch.id_branch = branch.generate_branch_id()
            branch.save()
            return branch


class BranchUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = BranchCompany
        fields = [
            'company',
            'title',
            'phone_number1',
            'phone_number2',
            'address',
            'region',
            'district',
            'delivery',
            'longitude',
            'latitude',
        ]

        def validate(self, attrs):
            if attrs.get('phone_number1') == attrs.get('phone_number2'):
                raise CustomExceptionError(code=400, detail='Phone numbers must be different.')
            return attrs