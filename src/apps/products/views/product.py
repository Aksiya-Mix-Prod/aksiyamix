from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.permissions import CustomIsCompanyOwnerOrReadOnlyPermission
from apps.products.serializers import ProductSerializer
from apps.base.exceptions import CustomExceptionError


class ProductCreateListViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, CustomIsCompanyOwnerOrReadOnlyPermission]

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise CustomExceptionError(code=400, detail=serializer.errors)


class ProductRetrieveUpdateDestroyViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, CustomIsCompanyOwnerOrReadOnlyPermission]

    def get_product(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise CustomExceptionError(code=404, detail="Product not found.")

    def retrieve(self, request, pk=None):
        product = self.get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise CustomExceptionError(code=400, detail=serializer.errors)

    def partial_update(self, request, pk=None):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise CustomExceptionError(code=400, detail=serializer.errors)

    def destroy(self, request, pk=None):
        product = self.get_product(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
