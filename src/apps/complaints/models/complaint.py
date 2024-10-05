from django.conf import settings
from django.db import models

from src.apps.companies.models.company import Company
from src.apps.base.models.base import AbstractBaseModel


class Complaint(AbstractBaseModel):
    """
    Here creating complaint of users
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True)
    company = models.ForeignKey(Company,
                                on_delete=models.SET_NULL,
                                null=True)

    message = models.CharField(max_length=200)
    first_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])

    viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name