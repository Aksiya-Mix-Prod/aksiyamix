from django.db import models

from apps.base.models import AbstractBaseModel


class Tag(AbstractBaseModel):
    name = models.SlugField(max_length=25)

    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name