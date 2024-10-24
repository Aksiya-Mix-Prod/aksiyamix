from django.db import models
from apps.base.models.base import AbstractBaseModel
from apps.discounts.models import Discount
from apps.discounts.validators.image_size import discount_image_size


class DiscountImage(AbstractBaseModel):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='discount/images/%Y/%m/%d/',
                              validators=[discount_image_size])
    ordering_number = models.PositiveSmallIntegerField()

    def save(self, *args, **kwargs):
        if self.discount:
            if self.ordering_number == 1:
                self.discount.image = self.image
                self.discount.save()

        super().save(*args, **kwargs)
