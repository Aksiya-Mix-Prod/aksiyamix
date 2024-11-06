from django.urls import path

<<<<<<< HEAD
from apps.products.views import (ProductCreateListViewSet,
                                 ProductRetrieveUpdateDestroyViewSet)

=======

from apps.products.views import ProductViewSet

>>>>>>> 3b3e1be4f5f24ff0cf98aca5480a35c567612966

urlpatterns = [
    path('', ProductCreateListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list-create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='product-detail'),
]
