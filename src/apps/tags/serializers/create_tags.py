from rest_framework import serializers

from apps.base.serializers import CustomSerializer
from apps.tags.models.tags import Tag


class TagsBulkCreateSerializer(CustomSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(max_length=25),
    )

    def save(self, **kwargs):
        all_tags = Tag.objects.all()
        tags = []
        data = []
        for tag in self.validated_data['tags']:
            if not tag in all_tags.values_list('name', flat=True):
                obj = Tag(name=tag)
                tags.append(obj)
                data.append({"id":obj.id, "name":obj.name})
            else:
                obj = all_tags.get(name=tag)
                data.append({"id":obj.id, "name":obj.name})
        Tag.objects.bulk_create(tags)
        self.validated_data['tags'] = data