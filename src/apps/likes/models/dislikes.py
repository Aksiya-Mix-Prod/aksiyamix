from django.db import models
from django.conf import settings

from apps.discounts.models import Discount
from apps.base.models import  AbstractBaseModel



class DiscountDislike(AbstractBaseModel):
    """
    :what: Model to track which user disliked what discount.
    :does: This connects a user and a discount with a dislike, and ensures
        each user can only dislike a specific discount once.
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_dislikes',
        limit_choices_to={
            'is_active': True,
            'is_spam':False,
        }
    )
    discount = models.ForeignKey(
        to='discounts.Discount',
        on_delete=models.CASCADE,
        null=True,
        related_name='discount_dislikes',
        limit_choices_to={
            'is_active': True,
            'status': Discount.Status.PROCESS
        }
    )

    class Meta:
        # ======== Ensure each user can only dislike a specific discount once =========
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'discount'],
                name='unique_user_discount_dislike'
            )
        ]
        ordering = ['-created_at']
        verbose_name = 'Discount Dislike'
        verbose_name_plural = 'Discount Dislikes'

    def __str__(self):
        """String representation for the DiscountDisLike model."""
        return f"Dislike: {self.user} disliked {self.discount.id} on {self.created_at}"
