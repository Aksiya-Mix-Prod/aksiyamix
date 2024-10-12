from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.base.models import AbstractBaseModel


class TopCalendar(AbstractBaseModel):
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    days = ArrayField(ArrayField(models.BooleanField()))

    class Meta:
        db_table = 'top_calendar'
        unique_together = ('year', 'month')

    def __str__(self):
        return f"{self.year}/{self.month}"