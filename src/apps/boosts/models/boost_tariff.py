from django.db import models

from src.apps.base.models import AbstractBaseModel


class BoostTariff(AbstractBaseModel):

    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
