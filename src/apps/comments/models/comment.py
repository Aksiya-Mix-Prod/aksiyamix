from django.db import models
from django.conf import settings

from apps.base.models.base import AbstractBaseModel
from apps.comments.validators import CommentValidator
from apps.comments.managers import CommentManager
from apps.discounts.models import Discount


class Comment(AbstractBaseModel):
    """
    Model to represent a comment.
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        limit_choices_to={
            'is_active': True,
            'is_spam': False,
            'is_deleted': False,
        }
    )
    discount = models.ForeignKey(
        to='discounts.Discount',
        on_delete=models.CASCADE,
        null=True,
        related_name='comments',
        limit_choices_to={
            'is_active': True,
            'status': Discount.Status.APPROVED,
        }
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        limit_choices_to={
            'is_deleted': False,
        }
    )
    is_deleted = models.BooleanField(default=False)
    text = models.CharField(max_length=255, validators=[CommentValidator(limit_value=255)])

    # ======= Filter out the is_deleted comments =======
    active_objects = CommentManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text