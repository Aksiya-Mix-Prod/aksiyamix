from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.tags.models import Tag


class SearchTagsGenericAPIView(GenericAPIView):
    """
    This view should return a list of filter startswith the tags
    """
    queryset = Tag.objects.all()

    def get(self, request, *args, **kwargs):
        data = self.queryset.filter(name__startswith=request.query_params.get('q', ''), 
                                    is_active=True).values('name')
        return Response(data, status=200)