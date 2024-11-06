from apps.advertisements.models.advertisement import Advertisement
from apps.base.serializers.model_serializer import CustomModelSerializer


class AdvertisementSerializer(CustomModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            "id_advertisement",
            "title",
            "image",
            "image2",
            "image3",
            "url_link",
            "ordering",
            "is_active",
            "start_date",
            "end_date",
        ]

        read_only_fields = ["id_advertisement"]
