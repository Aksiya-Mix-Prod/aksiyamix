from django.contrib.auth import get_user_model

from apps.base.serializers.model_serializer import CustomModelSerializer
from apps.comments.models import Comment
from apps.comments.paginations.paginations import CommentReplyPagination


class UserSerializer(CustomModelSerializer):
    """
    Serializer for User data to be included in Comment and CommentReply serializers.
    Using a separate UserSerializer provides flexibility and reusability, making it easier
    to include user-related fields and control user data representation in nested serializers.

    get_user_model() returns the actual user model class, so you can work directly with it. This is essential in
        serializers because model = settings.AUTH_USER_MODEL alone would raise an error,
        as it only provides a string, not a model reference.
    """
    class Meta:
        # ======== Specify the user model to dynamically handle custom user models if used. ========
        model = get_user_model()
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




