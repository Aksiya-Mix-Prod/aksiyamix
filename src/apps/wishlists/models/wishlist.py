from django.db import models

from apps.base.models import AbstractBaseModel


class WishList(AbstractBaseModel):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    discount = models.ForeignKey('discounts.Discount', on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlist'

    def __str__(self):
        return self.pk