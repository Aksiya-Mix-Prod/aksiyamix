from django.db import models
from django.core.validators import MinValueValidator

from apps.base.models import AbstractBaseModel


class TopTariff(AbstractBaseModel):
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    price = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'top_tariff'

    def __str__(self):
        return f"{self.quantity} - {self.price}"