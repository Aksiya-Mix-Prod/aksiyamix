from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

from apps.base.models import AbstractBaseModel


class TopDiscount(AbstractBaseModel):
    discount = models.ForeignKey('discounts.Discount', on_delete=models.CASCADE, related_name='top_discounts')
    dates = ArrayField(models.DateField())

    class Meta:
        db_table = 'top_discount'

    def __str__(self):
        return f"{self.price}-{self.quantity}"