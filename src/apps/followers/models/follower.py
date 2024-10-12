from django.db import models
from django.conf import settings

from src.apps.base.models.base import AbstractBaseModel
from src.apps.companies.models import Company


class Follower(AbstractBaseModel):
    """
    Here we will store the followers of the companies
    """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='followers')


    company = models.ForeignKey(Company,
                                on_delete=models.SET_NULL,
                                related_name='follower_of_companies')

