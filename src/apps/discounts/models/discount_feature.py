from django.core.validators import MinValueValidator
from django.db import models

from src.apps.base.exceptions import CustomExceptionError
from src.apps.base.models import AbstractBaseModel
from src.apps.base.serializers import CustomModelSerializer


class DiscountFeature(AbstractBaseModel):
    discount = models.ForeignKey('discounts.Discount', on_delete=models.CASCADE, related_name='discount_features')
    feature_value = models.ManyToManyField(
        to='features.FeatureValue',
        related_name='discount_features',
        limit_choices_to={
            'is_active': True,
        }
    )

    price = models.DecimalField(max_digits=30, decimal_places=2, validators=[MinValueValidator(0)])
    old_price = models.DecimalField(max_digits=30, decimal_places=2, validators=[MinValueValidator(0)])

    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    remainder = models.PositiveIntegerField()

    def clean(self):
        if self.old_price <= self.price:
            raise CustomExceptionError(code=400,
                                       detail={'old_price': "Old price must be greater than or equal to the price"})

        if self.remainder > self.quantity:
            raise CustomExceptionError(code=400,
                                       detail={'remainder': "Remainder must be less than or equal to the quantity"})

    def __str__(self):
        return f"{self.discount}"
