from django.db import models
from apps.base.exceptions import CustomExceptionError
from apps.base.models import AbstractBaseModel

class Packet(AbstractBaseModel):
    """
    Packet Model
    """
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.quantity

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Packet'
        verbose_name_plural = 'Packets'

