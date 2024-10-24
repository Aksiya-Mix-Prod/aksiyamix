from django.db import models
from django.conf import settings
from django.core.validators import ValidationError

from apps.base.models import AbstractBaseModel


class DiscountLike(AbstractBaseModel):
    """
    :what: Model to track which user liked what discount.
    :does: This connects a user and a discount with a like, and ensures
        each user can only like a specific discount once.
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_likes',
        limit_choices_to={
            'is_active': True,
            'is_spam':False,
        },
    )
    discount = models.ForeignKey(
        to='discounts.Discount',
        on_delete=models.CASCADE,
        related_name='discount_likes',
        limit_choices_to={
            'is_active': True,
            'status': 3
        }
    )

    class Meta:
        # ======== Ensure each user can only like a specific discount once =========
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'discount'],
                name='unique_user_discount_like'
            )
        ]

        ordering = ['-created_at']
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        """String representation for the DiscountLike model."""
        return f"Like: {self.user} liked {self.discount.title} on {self.created_at}"

    def clean(self):
        """ Override the clean method to validate status dynamically."""
        from apps.discounts.models import Discount
        if self.discount.status != Discount.Status.APPROVED:
            raise ValidationError("You can only like an approved discount.")