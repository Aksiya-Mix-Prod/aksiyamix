from django.db import models

from apps.base.models import AbstractBaseModel


class Tags(AbstractBaseModel):
    name = models.SlugField(max_length=25, unique=True)

    def __str__(self):
        return self.name