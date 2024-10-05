from rest_framework import serializers

from ..models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    """ Use teh same serializer for children serialization """

    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon', 'parent', 'created_at', 'children']

    def get_children(self, obj):
        """ Get category children """

        children = obj.children.all()
        if children.exists():
            return CategorySerializer(children, many=True).data
        return None
