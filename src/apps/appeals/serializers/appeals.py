from apps.appeals.models import Appeal
from apps.base.serializers import CustomModelSerializer


class AppealSerializer(CustomModelSerializer):
    """
    Appeal Serializer
    """

    class Meta:
        model = Appeal
        fields = ('company', 'phone_number', 'subject', 'message')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)