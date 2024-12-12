from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.base.views.generics import CustomGenericAPIView
from apps.tags.serializers import TagsBulkCreateSerializer
from apps.tops.permissions import IsCompanyOwner


class TagsCreateAPIView(CustomGenericAPIView):
    """
    Create tags for the current discount.
    """
    permission_classes = [IsAuthenticated, IsCompanyOwner]
    queryset = []
    serializer_class = TagsBulkCreateSerializer

    def post(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.validated_data, status=201)