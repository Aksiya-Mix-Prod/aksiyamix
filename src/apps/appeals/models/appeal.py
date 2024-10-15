from django.db import models
from django.conf import settings

from src.apps.base.models import AbstractBaseModel


class Appeal(AbstractBaseModel):
    """
    Model for clients to send appeals to admins.
    """

    # which user is sending appeal
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)

    # appeal for which company
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)

    # phone number of user
    phone_number = models.CharField(max_length=13)

    # subject of user
    subject = models.CharField(max_length=100)

    # message of appeal
    message = models.CharField(max_length=255)

    class Meta:
        db_table = "appeal"


