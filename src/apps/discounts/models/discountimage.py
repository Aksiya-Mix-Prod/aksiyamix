from src.apps.base import models
from src.apps.base.models.base import AbstractBaseModel
from src.apps.discounts.views import Discount


class DiscountImage(AbstractBaseModel):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='discount/images/%Y/%m/%d/',
                              validators=[validate_image_size])
    ordering_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
