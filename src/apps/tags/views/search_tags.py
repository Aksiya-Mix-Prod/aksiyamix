from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.base.serializers import EmptySerializer
from apps.base.views.generics import CustomGenericAPIView
from apps.tops.permissions import IsCompanyOwner
from apps.tags.models import Tag


class SearchTagsGenericAPIView(CustomGenericAPIView):
    permission_classes = [IsAuthenticated, IsCompanyOwner]
    """
    This view should return a list of filter startswith the tags
    """
    queryset = Tag.objects.all()
    serializer_class = EmptySerializer

    def get(self, request, *args, **kwargs):
        data = self.queryset.filter(name__startswith=request.query_params.get('q', '')
                                    ).values('id', 'name')
        return Response(data, status=200)