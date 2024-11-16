from apps.base.views import CustomReadOnlyModelViewSet
from apps.categories.models.category import Category
from apps.categories.serializers.categories import CategorySerializer


class CategoryListViewSet(CustomReadOnlyModelViewSet):
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer


class ChildrenCategoryViewSet(CustomReadOnlyModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        parent_id = self.kwargs['parent_id']
        return Category.objects.filter(parent_id=parent_id)




