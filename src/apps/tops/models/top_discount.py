from django.db import models
from django.contrib.postgres.fields import ArrayField

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