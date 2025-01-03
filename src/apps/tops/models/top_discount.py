from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.base.models import AbstractBaseModel
from apps.discounts.models import Discount


class TopDiscount(AbstractBaseModel):
    discount = models.ForeignKey(to='discounts.Discount',
                                 on_delete=models.PROTECT,
                                 related_name='top_discounts',
                                 limit_choices_to={
                                     'is_deleted': False,
                                     'is_active': True,
                                     'status': Discount.Status.APPROVED
                                    })
    dates = ArrayField(base_field=models.DateField())

    class Meta:
        db_table = 'top_discount'
        
    def clean(self):
        clone_dates = {}
        for date in self.dates:
            if str(date) not in clone_dates:
                clone_dates[str(date)] = -1
            clone_dates[str(date)] = clone_dates[str(date)] + 1
        for key, value in clone_dates.items():
            if value > 0:
                for i in range(value):
                    date_obj = datetime.strptime(key, "%Y-%m-%d").date()
                    self.dates.remove(date_obj)
        return super().clean()