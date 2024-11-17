from apps.base.serializers import CustomModelSerializer
from apps.categories.models.category import Category


class CategorySerializer(CustomModelSerializer):
    """
    Category Serializer
    """

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon', 'parent', 'created_at']

