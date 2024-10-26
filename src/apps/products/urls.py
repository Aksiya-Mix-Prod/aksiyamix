from django.urls import path
from apps.products.views import ProductViewSet

urlpatterns = [
    path('create/', ProductViewSet.as_view(), name='product_create'),
]
