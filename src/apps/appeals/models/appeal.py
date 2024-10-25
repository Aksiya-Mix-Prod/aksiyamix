from django.db import models
from django.conf import settings

from apps.base.models import AbstractBaseModel


class Appeal(AbstractBaseModel):
    """
    Appeal Model
    """

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        help_text='which user is sending appeal',
        limit_choices_to={"is_active": True, "is_spam": False},
    )

    company = models.ForeignKey(
        to='companies.Company',
        on_delete=models.CASCADE,
        help_text='appeal for which company'
    )

    phone_number = models.CharField(max_length=13, help_text='phone number of user')

    subject = models.CharField(max_length=100, help_text='subject of user')

    message = models.CharField(max_length=255, help_text='message of appeal')

    class Meta:
        db_table = "appeal"


