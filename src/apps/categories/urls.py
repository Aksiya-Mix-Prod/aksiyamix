from django.urls import path
from apps.categories.views.category import CategoryListViewSet


urlpatterns = [
    path('', CategoryListViewSet.as_view({'get': 'list'}), name="category-list"),
]
