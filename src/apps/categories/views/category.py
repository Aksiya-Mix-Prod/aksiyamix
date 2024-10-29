from jedi.inference.gradual.typeshed import try_to_load_stub_cached
from rest_framework.decorators import action
from rest_framework.response import Response
from yaml import serialize

from apps.base.exceptions import CustomExceptionError
from apps.categories.serializers.category import CategorySerializer
from apps.categories.models.category import Category
from apps.base.views import CustomViewSet, CustomModelViewSet


class CategoryListViewSet(CustomViewSet):

    def list(self, request):
        categories = Category.objects.filter(parent=None) # get parent(does not have parent) categories
        serializer = CategorySerializer(categories, many=True)
        return Response({'categories': serializer.data})




