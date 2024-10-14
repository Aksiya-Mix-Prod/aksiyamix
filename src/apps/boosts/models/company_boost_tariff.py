from django.db import models

from src.apps.base.models import AbstractBaseModel


class CompanyBoostTariff(AbstractBaseModel):

    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='company_boost_tariffs')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
