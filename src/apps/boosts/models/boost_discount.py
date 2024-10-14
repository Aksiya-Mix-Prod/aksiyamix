from django.db import models

from src.apps.base.models import AbstractBaseModel


class BoostTariff(AbstractBaseModel):

    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, related_name='boost_tariffs')