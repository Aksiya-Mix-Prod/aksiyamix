from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.base.pagination import CustomPageNumberPagination
from apps.base.views.viewsets import CustomGenericViewSet
from apps.comments.models import Comment
from apps.comments.permissions.permissions import IsAdminOrCommentOwner
from apps.comments.serializers.comments import (CommentReplySerializer,
                                                CommentSerializer)
from apps.discounts.models import Discount


class DiscountCommentViewSet(CustomGenericViewSet):
    """
    ViewSet for handling discount comments and replies:
    - Add/remove comments on discounts
    - Add/remove replies to comments
    - List comments and replies
    - Delete comments/replies (admin or owner only)
    """
    permission_classes = [IsAdminOrCommentOwner]
    pagination_class = CustomPageNumberPagination
    serializer_class = CommentSerializer

    def get_queryset(self) -> QuerySet:
        """
        Filter queryset based on the action being performed:
        - Returns parent comments for comment-related actions
        - Returns replies for reply-related actions
        """

        # ======== With 'select-related', we limit to Total: 1 database query instead of Total: 4 db queries.
        # select_related() uses JOINs and is for foreign key and one-to-one relationships ========
        base_queryset = Comment.active_objects.select_related('user', 'discount', 'parent')

        if self.action in ['list_comments', 'add_comment', 'delete_comment']:
            # ======== prefetch_related() (used for 'children') handles many-to-many and reverse foreign key
            # relationships ========
            return base_queryset.filter(parent__isnull=True).prefetch_related('children').order_by('-created_at')
        elif self.action in ['list_replies', 'add_reply', 'delete_reply']:
            return base_queryset.filter(parent__isnull=False).order_by('-created_at')

        return Comment.active_objects.none()

    def get_serializer_class(self):
        """
        Return appropriate serializer based on the action:
        - CommentSerializer for parent comments
        - CommentReplySerializer for replies
        """
        if self.action in ['add_reply', 'list_replies']:
            return CommentReplySerializer
        return CommentSerializer

    @action(detail=False, methods=['get'], url_path='comments')
    def list_comments(self, request) -> Response:
        """
        List all parent comments for a discount:
        - Returns paginated list of comments
        - Ordered by most recent first
        - Includes nested replies
        """
        discount_id = request.query_params.get('discount_id')
        if not discount_id:
            return Response(
                {"error":"discount_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        queryset = self.get_queryset().filter(discount_id=discount_id)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['post'], url_path='add-comment')
    def add_comment(self, request) -> Response:
        """
        Add a new parent comment to a discount:
        - Requires discount_id and content in request data
        - Associates comment with current user
        """
        discount = get_object_or_404(Discount, id=request.data.get('discount'))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(
            user=request.user, discount=discount
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'], url_path='delete-comment')
    def delete_comment(self, request, pk=None) -> Response:
        """
        Delete a parent comment:
        - Only admin or comment owner can delete
        - Soft deletes the comment and all its replies
        """
        comment = self.get_object()
        comment.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='replies')
    def list_replies(self, request) -> Response:
        """
        List all replies for a specific parent comment:
        - Returns paginated list of replies
        - Ordered by most recent first
        """
        parent_id = request.query_params.get('parent_id')
        if not parent_id:
            return Response(
                {"error":"parent_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        queryset = self.get_queryset().filter(parent_id=parent_id)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['post'], url_path='add-reply')
    def add_reply(self, request) -> Response:
        """
        Add a reply to a parent comment:
        - Requires parent_id and content in request data
        - Associates reply with current user and parent comment's discount
        """
        parent = get_object_or_404(Comment, id=request.data.get('parent'))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(
            user=request.user, discount=parent.discount, parent=parent
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'], url_path='delete-reply')
    def delete_reply(self, request, pk=None) -> Response:
        """
        Delete a reply:
        - Only admin or reply owner can delete
        - Soft deletes the reply
        """
        reply = self.get_object()
        reply.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)