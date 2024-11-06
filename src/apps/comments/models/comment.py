from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models.base import AbstractBaseModel
from apps.comments.managers import CommentManager
from apps.comments.validators import CommentValidator
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
        },
        help_text=_("The user who created this comment. Only active, non-spam, non-deleted users are allowed.")
    )
    discount = models.ForeignKey(
        to='discounts.Discount',
        on_delete=models.CASCADE,
        null=True,
        related_name='comments',
        limit_choices_to={
            'is_active': True,
            'status': Discount.Status.APPROVED,
        },
        help_text=_("The discount this comment is related to. Only active and approved discounts are allowed.")
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        limit_choices_to={
            'is_deleted': False,
        },
        help_text=_("The parent comment if this is a reply. Only non-deleted comments can be parents.")
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text=_("Indicates if the comment is marked as deleted.")
    )
    text = models.CharField(
        max_length=255,
        validators=[CommentValidator(limit_value=255)],
        help_text=_("The content of the comment, up to 255 characters.")
    )

    # ======= Filter out the is_deleted comments =======
    active_objects = CommentManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text
