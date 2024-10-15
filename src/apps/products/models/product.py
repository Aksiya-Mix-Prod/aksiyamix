from itertools import product

from django.db import models
from src.apps.base.models.base import AbstractBaseModel

class Product(AbstractBaseModel):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='products')

    title = models.CharField(max_length=200)
    image  = models.ImageField(upload_to='product/images/%Y/%m/%d/',
                              validators=[validate_image_size])

    def __str__(self):
        return self.title