from django.db import models

from src.apps.companies.choice.country import Country
from src.apps.companies.choice.disctrict import District
from src.apps.base.models.base import AbstractBaseModel


class BranchCompany(AbstractBaseModel):
    """
    Here creating branch Company
    """
    company = models.ForeignKey('Company', on_delete=models.PROTECT)

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    address = models.CharField(max_length=255)

    country = models.PositiveSmallIntegerField(choices=Country.choices)
    district = models.PositiveSmallIntegerField(choices=District.choices)

    delivery = models.BooleanField(default=False)

    longitude = models.FloatField()
    latitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def get_address(self):
        return {
            'address': self.address,
            'longitude': self.longitude,
            'latitude': self.latitude
        }

    def __str__(self):
        return self.name