from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.categories.views.category import CategoryListViewSet, ChildrenCategoryViewSet


urlpatterns = [
    path('', CategoryListViewSet.as_view({'get': 'list'}), name='category-list'),
    path('get-children/<slug:parent_id>/', ChildrenCategoryViewSet.as_view({'get': 'list'}), name='children-category'),
]

