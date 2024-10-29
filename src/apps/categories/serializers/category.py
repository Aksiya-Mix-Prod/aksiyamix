from rest_framework import serializers

from apps.categories.models.category import Category
from apps.base.serializers import CustomModelSerializer


class CategorySerializer(CustomModelSerializer):
    """
    Category Serializer
    """

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon', 'parent', 'created_at']


    def get_children(self, slug):
        """ Get category children """

        children = Category.objects.filter(parent_id=slug)
        if children.exists():
            return CategorySerializer(children, many=True).data
        return None


