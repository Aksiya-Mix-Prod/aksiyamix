import uuid

from django.conf import settings
from django.db import models

from apps.base.services import normalize_txt


class AbstractBaseModel(models.Model):
    """ General abstract base model """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        null=True,
        blank=True,
        editable=False,
        related_name='+'
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        null=True,
        blank=True,
        editable=False,
        related_name='+'
    )

    def save(self, *args, **kwargs):
        """ Normalize text fields before saving """
        normalize_txt(self)
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
