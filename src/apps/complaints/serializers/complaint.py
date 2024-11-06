from apps.base.exceptions import CustomExceptionError
from apps.base.serializers.model_serializer import CustomModelSerializer
from apps.complaints.models.complaint import Complaint


class ComplaintSerializer(CustomModelSerializer):
    class Meta:
        model = Complaint
        fields = ['user', 'discount', 'comment', 'company', 'complaint_types', 'message', 'first_name',
                  'viewed', 'is_completed']
        read_only_fields = ['viewed', 'is_completed']

    def create(self, validated_data):
        return Complaint.objects.create(**validated_data)

    def validate_first_name(self, value):
        """Check if first name have not"""
        if not value:
            return CustomExceptionError(code=400, detail="First name is required")
        return value

    def validate_message(self, value):
        """Check if message have not"""
        if not value:
            return CustomExceptionError(code=400, detail="Message cannot be empty")
        return value
