from apps.base.models import AbstractBaseModel
from apps.discounts.models import Discount
from django.conf import settings
from django.db import models


class Wishlist(AbstractBaseModel):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    discount = models.ForeignKey(
        to="discounts.Discount",
        on_delete=models.CASCADE,
        limit_choices_to={
            "is_deleted": False,
            "is_active": True,
            "status": Discount.Status.APPROVED,
        },
        related_name="wishlists",
    )

    class Meta:
        db_table = "wishlist"

    def __str__(self):
        return str(self.pk)
