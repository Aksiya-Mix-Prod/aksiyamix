from django.db import models
from django.core.validators import MinValueValidator

from apps.base.exceptions import CustomExceptionError


class General(models.Model):
    """
    General Model
    """

    min_replenishment_amount = models.CharField(max_length=100,
                                                help_text='minimum amount of company balance replenishment')
    max_replenishment_amount = models.CharField(max_length=100,
                                                help_text='maximum amount of company balance replenishment')

    def save(self, *args, **kwargs):
        if self.min_replenishment_amount >= self.max_replenishment_amount:
            raise CustomExceptionError(
                code=400,
                detail={
                    "min_replenishment_amount": "min_replenishment_amount should be less than max_replenishment_amount"
                }
            )

        super().save(*args, *kwargs)

    class Meta:
        db_table = "general"


class Currency(models.Model):
    """
    Currency Model
    """

    one_usd_in_uzs = models.DecimalField(
        max_digits=30,
        decimal_places=1,
        validators=[MinValueValidator(0)],
        help_text='howmuch is one usd in one uzs'
    )

    date = models.DateField(auto_now_add=True, help_text='date when usd value for uzs updated')

    class Meta:
        db_table = "currency"
