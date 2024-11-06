from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.base.serializers import CustomModelSerializer


class UserProfileRetrieveUpdateModelSerializer(CustomModelSerializer):
    gender = serializers.CharField(source="get_gender_display", required=False)
    region = serializers.CharField(source="get_region_display", required=False)
    district = serializers.CharField(source="get_district_display", required=False)

    class Meta:
        fields = ["id", "username", "fullname", "email", "phone_number", 
                  "birthday", "gender", "region", "district"]
        model = get_user_model()
        read_only_fields = ["id", "username"]
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        print(attrs)
        user = get_user_model().objects.get(id=self.context["request"].user.id)
        print(attrs, user)
        return attrs