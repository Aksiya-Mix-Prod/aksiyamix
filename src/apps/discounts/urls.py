from django.urls import path

from apps.discounts.views import DiscountCreateListViewSet, DiscountRetrieveUpdateDestroyViewSet

urlpatterns = [
    path('', DiscountCreateListViewSet.as_view({'get': 'list', 'post': 'create'}), name='discount-list'),
    path('<int:pk>/', DiscountRetrieveUpdateDestroyViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='discount-detail'),
]
