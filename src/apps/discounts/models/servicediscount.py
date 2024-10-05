from django.db import models
from src.apps.base.models.base import AbstractBaseModel
from src.apps.general.validate_file_size import validate_icon_size, validate_image_size


class ServiceDiscount(AbstractBaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    icon = models.ImageField(upload_to='discount/icons/%Y/%m/%d/',
                             validators=[validate_icon_size],
                             blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
