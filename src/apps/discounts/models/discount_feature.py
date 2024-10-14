from django.db import models

from src.apps.base.models import AbstractBaseModel


class DiscountFeature(AbstractBaseModel):
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, related_name='discount_features')
    feature_value = models.ForeignKey('FeatureValue', on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)