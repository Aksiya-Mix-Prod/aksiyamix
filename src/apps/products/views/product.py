from rest_framework.generics import CreateAPIView
from src.apps.products.models import Product

from src.apps.products.serializers import ProductSerializer

class ProductCreateView(CreateAPIView):
    """
    View for creating a new product.
    """
    permission_classes = []
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
