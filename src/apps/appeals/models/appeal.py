from django.conf import settings
from django.db import models

from apps.base.models import AbstractBaseModel


class Appeal(AbstractBaseModel):
    """
    Appeal Model
    """

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={"is_active": True, "is_spam": False},
        help_text='which user is sending appeal'
    )

    company = models.ForeignKey(
        to='companies.Company',
        on_delete=models.CASCADE,
        limit_choices_to={'is_active': True, 'is_verified': True, 'is_deleted': False},
        help_text='appeal for which company'
    )

    phone_number = models.CharField(max_length=13, help_text='phone number of user')

    subject = models.CharField(max_length=100, help_text='subject of user')

    message = models.CharField(max_length=255, help_text='message of appeal')

    class Meta:
        db_table = "appeal"


    def __str__(self):
        return self.message


