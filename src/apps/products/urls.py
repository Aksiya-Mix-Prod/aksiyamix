from django.urls import path
from apps.products.views import ProductCreateListViewSet, ProductRetrieveUpdateDestroyViewSet

urlpatterns = [
    path('', ProductCreateListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list-create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='product-detail'),
]
