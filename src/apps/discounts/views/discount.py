from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from apps.base.exceptions import CustomExceptionError
from apps.discounts.serializers import DiscountCreateUpdateSerializer
from apps.products.models import Product

from rest_framework.response import Response


class DiscountCreateListViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        product = Product.objects.all()
        serializer = DiscountCreateUpdateSerializer(product, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DiscountCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise CustomExceptionError(code=400, detail=serializer.errors)


class DiscountRetrieveUpdateDestroyViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_discount(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise CustomExceptionError(code=404, detail="Discount not found.")

    def retrieve(self, request, pk=None):
        discount = self.get_discount(pk)
        serializer = DiscountCreateUpdateSerializer(discount)
        return Response(serializer.data)

    def update(self, request, pk=None):
        discount = self.get_discount(pk)
        serializer = DiscountCreateUpdateSerializer(discount, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise CustomExceptionError(code=400, detail=serializer.errors)

    def partial_update(self, request, pk=None):
        discount = self.get_discount(pk)
        serializer = DiscountCreateUpdateSerializer(discount, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise CustomExceptionError(code=400, detail=serializer.errors)

    def destroy(self, request, pk=None):
        discount = self.get_discount(pk)
        discount.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)