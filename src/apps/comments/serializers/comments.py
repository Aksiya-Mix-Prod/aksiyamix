from django.conf import settings

from apps.comments.models import Comment
from apps.base.serializers.model_serializer import CustomModelSerializer
from apps.comments.paginations.paginations import CommentReplyPagination


class UserSerializer(CustomModelSerializer):
    """

    """
    class Meta:
        user = settings.AUTH_USER_MODEL
        fields = ['id', 'username']


class CommentReplySerializer(CustomModelSerializer):
    """
    Serializer for child comments
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at', 'is_deleted']
        read_only_fields = ['is_deleted']


class CommentSerializer(CustomModelSerializer):
    """
    Serializer for Parent comments
    """
    user = UserSerializer(read_only=True)
    children = CommentReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'discount', 'text', 'created_at', 'is_deleted', 'children']
        read_only_fields = ['is_deleted']

    def get_children(self, obj):
        paginator = CommentReplyPagination()
        children = obj.children.filter(is_deleted=False).order_by('-created_at')
        paginated_children = paginator.paginate_queryset(children, self.context.get('request'))
        serializer = CommentReplySerializer(paginated_children, many=True)
        return {
            'results': serializer.data,
            'count': obj.children.filter(is_deleted=False).count(),
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link()
        }




