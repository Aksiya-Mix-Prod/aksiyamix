from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.tags.serializers import TagsBulkCreateSerializer
from apps.base.views.generics import CustomGenericAPIView


class TagsCreateAPIView(CustomGenericAPIView):
    """
    Create tags for the current discount.
    """
    permission_classes = (IsAuthenticated,)
    queryset = []
    serializer_class = TagsBulkCreateSerializer

    def post(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.validated_data, status=201)