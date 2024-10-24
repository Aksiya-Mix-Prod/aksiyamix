from django.db import models

from apps.companies.choice.country import Country
from apps.companies.choice.disctrict import District
from apps.base.models.base import AbstractBaseModel
from apps.users.validators.phone_number import phone_validate


class BranchCompany(AbstractBaseModel):
    """
    Here creating branch Company
    """
    company = models.ForeignKey('Company', on_delete=models.PROTECT,
                                related_name='branch_companies',
                                limit_choices_to={
                                    'is_active': True,
                                    'is_verified': True,
                                    'is_deleted': False
                                })

    title = models.CharField(max_length=255)
    phone_number1 = models.CharField(max_length=13, validators=[phone_validate])
    phone_number2 = models.CharField(max_length=13, validators=[phone_validate])
    address = models.CharField(max_length=255)

    country = models.PositiveSmallIntegerField(choices=Country.choices)
    district = models.PositiveSmallIntegerField(choices=District.choices)

    delivery = models.BooleanField(default=False)

    longitude = models.FloatField()
    latitude = models.FloatField()

    def get_address(self):
        return {
            'address': self.address,
            'longitude': self.longitude,
            'latitude': self.latitude
        }

    def __str__(self):
        return self.title