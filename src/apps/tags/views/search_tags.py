from rest_framework.response import Response

from apps.tags.models import Tag
from apps.base.views.generics import CustomGenericAPIView


class SearchTagsGenericAPIView(CustomGenericAPIView):
    """
    This view should return a list of filter startswith the tags
    """
    queryset = Tag.objects.all()
    serializer_class = None

    def get(self, request, *args, **kwargs):
        data = self.queryset.filter(name__startswith=request.query_params.get('q', '')
                                    ).values('id', 'name')
        return Response(data, status=200)