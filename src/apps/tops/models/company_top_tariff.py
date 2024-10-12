from django.db import models
from django.core.validators import MinValueValidator

from apps.base.models import AbstractBaseModel


class CompanyTopTariff(AbstractBaseModel):
    company = models.ForeignKey('companies.Company', on_delete=models.SET_NULL, related_name='top_tariffs')

    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.quantity}-{self.price}"