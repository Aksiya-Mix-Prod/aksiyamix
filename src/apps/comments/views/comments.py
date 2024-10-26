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
    ViewSet for handling discount comments and replies:
    - Add/remove comments on discounts
    - Add/remove replies to comments
    - List comments and replies
    - Delete comments/replies (admin or owner only)
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrCommentOwner]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        """
        Filter queryset based on the action being performed:
        - Returns parent comments for comment-related actions
        - Returns replies for reply-related actions
        """
        return (Comment.active_objects
                .filter(parent__isnull=True)
                .select_related('user', 'discount')
                .prefetch_related('children')
                .order_by('-created_at')
        """
        Return appropriate serializer based on the action:
        - CommentSerializer for parent comments
        - CommentReplySerializer for replies
        """
        """
        List all parent comments for a discount:
        - Returns paginated list of comments
        - Ordered by most recent first
        - Includes nested replies
        """
            )

    def create(self, request, *args, **kwargs):
        # ======== Get the discount and validate it exists ========
        """
        Add a new parent comment to a discount:
        - Requires discount_id and content in request data
        - Associates comment with current user
        """
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
        """
        Delete a parent comment:
        - Only admin or comment owner can delete
        - Soft deletes the comment and all its replies
        """

    Using CustomGenericViewSet as base class for consistent behavior
    """
    serializer_class = CommentReplySerializer
    permission_classes = [IsAuthenticated, IsAdminOrCommentOwner]
        """
        List all replies for a specific parent comment:
        - Returns paginated list of replies
        - Ordered by most recent first
        """

    def get_queryset(self):
        return (Comment.active_objects
                .filter(parent__isnull=True)
                .select_related('user', 'discount', 'parent')
                .order_by('-created_at')
            )

    def create(self, request, *args, **kwargs):
        # ========= Get and validate the parent comment exists =========
        """
        Add a reply to a parent comment:
        - Requires parent_id and content in request data
        - Associates reply with current user and parent comment's discount
        """
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






        """
        Delete a reply:
        - Only admin or reply owner can delete
        - Soft deletes the reply
        """