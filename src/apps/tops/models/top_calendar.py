from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.base.models import AbstractBaseModel


class TopCalendar(AbstractBaseModel):
    """ 
        This model shows booked days in month section!

        Fields:
                year: (int): A PositiveSmallIntegerField representing the year.
                month: (int): A PositiveSmallIntegerField representing the month (between 1 and 12).
                days: (List[List[bool]]): An ArrayField of ArrayField of BooleanField representing the booked days in the month. 
    """

    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    days = ArrayField(default=list,
        base_field=ArrayField(
            base_field=models.BooleanField(default=False), size=3))

    class Meta:
        db_table = 'top_calendar'
        unique_together = ('year', 'month')

    def __str__(self):
        return f"{self.year}/{self.month}"