from django.urls import path

from apps.categories.views.categories import (CategoryListViewSet,
                                              ChildrenCategoryViewSet)

urlpatterns = [
    path('', CategoryListViewSet.as_view({'get': 'list'}), name='category-list'),
    path('get-children/<slug:parent_id>/', ChildrenCategoryViewSet.as_view({'get': 'list'}), name='children-category'),
]

