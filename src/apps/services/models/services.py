from django.db import models
from django.utils.text import slugify

from apps.base.models import AbstractBaseModel
from apps.base.exceptions import CustomExceptionError
from apps.services.validators.image_size import service_image_size


class Service(AbstractBaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    icon = models.ImageField(upload_to='services/icon/%Y/%m/%d/', 
                             validators=[service_image_size], 
                             blank=True, null=True)

    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'service'

    def clean(self):
        self.slug = slugify(self.name)
        not_unique = Service.objects.filter(slug=self.slug, is_active=True).exists()
        if not_unique:
            raise CustomExceptionError(code=400, detail={'slug': 'Slug and is active must be unique'})
        if self.is_active and not self.icon:
            raise CustomExceptionError(code=400, detail={'icon': 'Icon is required when service is active'})            

    def __str__(self):
        return self.name