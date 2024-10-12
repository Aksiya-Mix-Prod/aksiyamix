from django.db import models

from apps.users.models import CustomUser
from apps.base.models.base import AbstractBaseModel
# from apps.discounts.models import Discount
from apps.comments.validators import CommentValidator
from apps.comments.managers import CommentManager


class Comment(AbstractBaseModel):
    """
    Model to represent a comment.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
   # discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    comment = models.CharField(max_length=500, validators=[CommentValidator(limit_value=500)])

    # ======= Delete this once CustomBaseModel is ready =======
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ======= Filter out the is_deleted comments =======
    objects = CommentManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
