from django.db import models

from apps.base.models import AbstractBaseModel
from apps.services.validators.image_size import service_image_size



class Service(AbstractBaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    icon = models.ImageField(upload_to='discount/icon/%Y/%m/%d/', validators=[service_image_size], blank=True, null=True)

    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'service'

    def __str__(self):
        return self.name