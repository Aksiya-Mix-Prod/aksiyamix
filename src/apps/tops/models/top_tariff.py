from django.core.validators import MinValueValidator
from django.db import models

from apps.base.exceptions import CustomExceptionError
from apps.base.models import AbstractBaseModel


class TopTariff(AbstractBaseModel):
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    price = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'top_tariff'

    def clean(self):
        top_tariffs = TopTariff.objects.all()
        for top_tariff in top_tariffs:
            if top_tariff.id != self.id and top_tariff.quantity == self.quantity:
                raise CustomExceptionError(code=400, detail=f"TopTariff with quantity {self.quantity} already exists.")
            if top_tariff.quantity > self.quantity and top_tariff.price < self.price:
                raise CustomExceptionError(code=400, detail=f"TopTariff with quantity {self.quantity} has lower price than {top_tariff.quantity}.")

    def __str__(self):
        return f"{self.quantity} - {self.price}"