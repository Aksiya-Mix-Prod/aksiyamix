from django.db import models

from apps.categories.models import Category
from apps.discounts.models import Discount
from src.apps.advertisements.validators import validate_image_size


class Advertisement(models.Model):
    """
    Here creating Advertisement model of Companies
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    start_date = models.DateField()
    end_date = models.DateField()

    image = models.ImageField(upload_to='advertisement/images/%Y/%m/%d/',
                              validators=[validate_image_size])

    sale_price = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('category', 'discount'),)

    def __str__(self):
        return self.title
