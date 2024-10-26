from rest_framework import mixins, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.comments.models import Comment
from apps.discounts.models import Discount
from apps.base.views import CustomGenericViewSet
from apps.comments.permissions.permissions import IsAdminOrCommentOwner
from apps.base.pagination import CustomPageNumberPagination
from apps.comments.serializers.comments import CommentSerializer, CommentReplySerializer



class CommentViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     CustomGenericViewSet):
    """
    ViewSet for handling parent comments:
    - List all parent comments
    - Create new comments
    - Delete comments (admin or owner only)

    Using CustomGenericViewSet as base class for consistent behavior
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrCommentOwner]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        """
        Return only the root comments (no parent) ordered by creation date.
        """
        return (Comment.active_objects
                .filter(parent__isnull=True)
                .select_related('user', 'discount')
                .prefetch_related('children')
                .order_by('-created_at')
            )

    def create(self, request, *args, **kwargs):
        # ======== Get the discount and validate it exists ========
        discount = get_object_or_404(Discount, id=request.data.get('discount'))

        # ======== Create serializer with the user and validated discount ========
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # ======== Save with the current user ========
        serializer.save(
            user=request.user,
            discount=discount
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentReplyViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          CustomGenericViewSet
                          ):
    """
     ViewSet for handling comment replies:
    - List all replies
    - Create new replies
    - Delete replies (admin or owner only)

    Using CustomGenericViewSet as base class for consistent behavior
    """
    serializer_class = CommentReplySerializer
    permission_classes = [IsAuthenticated, IsAdminOrCommentOwner]

    def get_queryset(self):
        return (Comment.active_objects
                .filter(parent__isnull=True)
                .select_related('user', 'discount', 'parent')
                .order_by('-created_at')
            )

    def create(self, request, *args, **kwargs):
        # ========= Get and validate the parent comment exists =========
        parent = get_object_or_404(Comment, id=request.data.get('parent'))

        # ======== Create serializer with the user and validated parent ========
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # ========= Save with the current user and parent ========
        serializer.save(
            user=request.user,
            discount=parent.discount,
            parent=parent
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)





