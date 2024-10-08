from rest_framework.response import Response
from rest_framework import generics

from ..serializers.category import CategorySerializer
from ..models.category import Category


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None) # get only parent categories
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        """ Convert categories to "categories" as list """

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({'categories': serializer.data})



