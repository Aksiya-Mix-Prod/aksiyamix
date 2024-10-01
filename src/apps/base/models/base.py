import uuid

from django.db import models
from django.conf import settings

from apps.base.services import normalize_txt


class AbstractBaseModel(models.Model):
    """ General abstract base model """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    updated_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )

    def save(self, *args, **kwargs):
        normalize_txt(self)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
