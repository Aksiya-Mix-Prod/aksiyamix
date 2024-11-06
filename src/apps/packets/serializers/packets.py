from apps.base.serializers.model_serializer import CustomModelSerializer
from apps.packets.models import Packet


class PacketSerializer(CustomModelSerializer):
    class Meta:
        model = Packet
        fields = ['id', 'quantity', 'price']

        # ========= Set all fields as read-only ========
        read_only_fields = fields
