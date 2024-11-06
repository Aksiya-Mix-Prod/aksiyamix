from django.conf import settings
from django.db import models

from apps.base.exceptions import CustomExceptionError
from apps.base.models.base import AbstractBaseModel


class Follower(AbstractBaseModel):
    """
    Here we will store the followers of the companies
    """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='followers')

    company = models.ManyToManyField('companies.Company',
                                     related_name='follower_of_companies')


    def clean(self):
        # Ensure that the user does not follow the same company multiple times
        for company in self.company.all():
            if Follower.objects.filter(user=self.user, company=company).exists():
                raise CustomExceptionError(code=400,
                                           detail={'user': f'You are already following the {company} company.'})

