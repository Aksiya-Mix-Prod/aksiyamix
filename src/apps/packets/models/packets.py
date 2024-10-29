from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal
from django.utils.translation import gettext_lazy as _
from apps.base.models import AbstractBaseModel

class Packet(AbstractBaseModel):
    """
    Packet Model for Payments
    """
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text=_("Number of times that can be used for posting discounts")
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=3,
        validators=[MinValueValidator(Decimal('1000'))],
        help_text=_("Price of the package in UZS")
    )

    def __str__(self):
        return self.quantity

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Packet'
        verbose_name_plural = 'Packets'

