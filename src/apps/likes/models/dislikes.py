from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.base.models import  AbstractBaseModel
from apps.discounts.models import Discount


class DiscountDislike(AbstractBaseModel):
    """
    :what: Model to track which user disliked what discount.
    :does: This connects a user and a discount with a dislike, and ensures
        each user can only dislike a specific discount once and cannot
        simultaneously like and dislike the same discount.
    """
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_dislikes',
        limit_choices_to={
            'is_active':True,
            'is_spam':False,
            'is_deleted':False
        },
        help_text=_("The user who disliked this discount. Only active, non-spam, and non-deleted users are allowed.")
    )
    discount = models.ForeignKey(
        to='discounts.Discount',
        on_delete=models.CASCADE,
        related_name='discount_dislikes',
        limit_choices_to={
            'is_active': True,
            'status': Discount.Status.APPROVED
        },
        help_text=_("The discount that was disliked. Only active and approved discounts are allowed.")
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
        """String representation for the DiscountDislike model."""
        return self.user or self.discount

    def clean(self):
        """Ensure user cannot simultaneously like and dislike a discount."""
        if self.user and self.discount:
            if self.discount.discount_dislikes.filter(user=self.user).exists():
                raise ValidationError(
                    """User cannot like and dislike the same discount simultaneously."""
                )
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)




