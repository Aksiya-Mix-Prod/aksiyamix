from django.db import models
from django.core.validators import MinValueValidator

from apps.base.models import AbstractBaseModel


class TopTariff(AbstractBaseModel):
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'top_tariff'

    def __str__(self):
        return f"{self.quantity} - {self.price}"