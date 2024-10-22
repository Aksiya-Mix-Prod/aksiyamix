from django.db import models
from django.conf import settings

from apps.companies.models import Company
from apps.base.models.base import AbstractBaseModel


class Follower(AbstractBaseModel):
    """
    Here we will store the followers of the companies
    """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='followers',
                                 limit_choices_to={
                                     'is_active': True,
                                     'is_spam': False
                                 })


    company = models.ForeignKey(Company,
                                on_delete=models.SET_NULL,
                                related_name='follower_of_companies',
                                null=True,
                                )

