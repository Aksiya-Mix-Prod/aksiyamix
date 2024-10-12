from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

from apps.base.models import AbstractBaseModel


class TopDiscount(AbstractBaseModel):
    discount = models.ForeignKey('discounts.Discount', on_delete=models.CASCADE, related_name='top_discounts')
    dates = ArrayField(models.DateField())

    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'top_discount'

    def __str__(self):
        return f"{self.price}-{self.quantity}"