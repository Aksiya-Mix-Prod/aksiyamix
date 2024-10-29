import random

from django.db import models

from apps.companies.choice.country import Country
from apps.companies.choice.disctrict import District
from apps.base.models.base import AbstractBaseModel
from apps.users.validators.phone_number import phone_validate


class BranchCompany(AbstractBaseModel):
    """
    Here creating branch Company
    """
    company = models.ForeignKey('companies.Company', on_delete=models.PROTECT,
                                related_name='branch_companies',
                                limit_choices_to={
                                    'is_active': True,
                                    'is_verified': True,
                                    'is_deleted': False
                                })

    id_branch = models.PositiveSmallIntegerField(unique=True, editable=False)
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

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.id_branch = self.generate_branch_id()
        super().save(*args, **kwargs)

    def generate_branch_id(self):
        while True:
            # Generate an 8-digit number

            new_id = random.randint(10000000, 99999999)

            # Check for uniqueness

            if not BranchCompany.objects.filter(id_branch=new_id).exists():
                return new_id

    def __str__(self):
        return self.title