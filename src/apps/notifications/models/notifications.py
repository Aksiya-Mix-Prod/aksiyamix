from django.db import models

from apps.base.models import AbstractBaseModel


class Notification(AbstractBaseModel):
    company = models.ForeignKey("companies.Company", on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title