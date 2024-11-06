from apps.base.serializers import CustomModelSerializer
from apps.companies.models.company_time_table import CompanyTimeTable


class CompanyTimeTableListSerializer(CustomModelSerializer):

    class Meta:
        model = CompanyTimeTable
        fields = ('company', 'branch_company', 'id_company_time_table', 'week_day', 'start_time', 'end_time')
        read_only_fields = ['id_company_time_table']


class CompanyTimeTableCreateUpdateSerializer(CustomModelSerializer):

    class Meta:
        model = CompanyTimeTable
        fields = ('company', 'branch_company', 'id_company_time_table', 'week_day', 'start_time', 'end_time')
        read_only_fields = ['id_company_time_table']

    """
    Override create to ensure a unique ID is generated.
    """
    def create(self, validated_data):
        instance = CompanyTimeTable.objects.create(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validate_data):
        instance.company = validate_data.get('company', instance.company)
        instance.branch_company = validate_data.get('branch_company', instance.branch_company)
        instance.week_day = validate_data.get('week_day', instance.week_day)
        instance.start_time = validate_data.get('start_time', instance.start_time)
        instance.end_time = validate_data.get('end_time', instance.end_time)
        instance.save()
        return instance


class CompanyTimeTableRetrieveSerializer(CustomModelSerializer):
    class Meta:
        model = CompanyTimeTable
        fields = ('company', 'branch_company', 'id_company_time_table', 'week_day', 'start_time', 'end_time')
        read_only_fields = ['id_company_time_table']
