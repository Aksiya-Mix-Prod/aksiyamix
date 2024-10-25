import random

from django.db import models
from django.conf import settings
from django.db.models import TextField
from django.core.validators import ValidationError


from apps.companies.choice.country import Country
from apps.base.models.base import AbstractBaseModel
from apps.categories.models.category import Category
from apps.companies.choice.disctrict import District
from apps.users.validators.phone_number import phone_validate
from apps.general.validators.youtobe_url import validate_youtube_url

from apps.companies.validators.company_video_size import validate_company_video_size
from apps.companies.validators.company_logo_size import (validate_company_logo_size, validate_logo_size)
from apps.companies.validators.company_banner_size import validate_company_banner_size, validate_banner_size


class Company(AbstractBaseModel):
    """Company model"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.PROTECT,
                              limit_choices_to={
                                  'is_active': True,
                                  'is_deleted': False
                            }
    )
    categories = models.ManyToManyField(Category, blank=True, related_name='companies')

    #   BIO FOR CREATE COMPANY ------ Here create of Owner

    owner_last_name = models.CharField(max_length=120)
    owner_first_name = models.CharField(max_length=120)
    owner_father_name = models.CharField(max_length=120)
    owner_phone_number1 = models.CharField(max_length=13, validators=[phone_validate])
    owner_phone_number2 = models.CharField(max_length=13, validators=[phone_validate])

    #   CREATE COMPANY ------- Here files of Company

    logo = models.ImageField(upload_to='companies/logos/%Y/%m/%d/',
                             validators=[validate_company_logo_size,
                                         validate_logo_size],
                             blank=True, null=True)

    video_url = models.URLField(
        validators=[validate_youtube_url],
        blank=True,
        null=True
    )

    banner = models.ImageField(upload_to='companies/banners/%Y/%m/%d/',
                               validators=[validate_company_banner_size,
                                           validate_banner_size],
                               blank=True, null=True)

    #   CREATE COMPANY ---------- Here all need things of Company

    country = models.PositiveSmallIntegerField(choices=Country.choices)
    district = models.PositiveSmallIntegerField(choices=District.choices)

    name = models.CharField(max_length=250)
    username = models.SlugField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_spammed = models.BooleanField(default=False)

    id_company = models.PositiveSmallIntegerField(unique=True, editable=False, null=True)

    follower_counts = models.CharField(max_length=40, default='0')
    like_counts = models.CharField(max_length=40, default='0')
    dislike_counts = models.CharField(max_length=40, default='0')
    comment_counts = models.CharField(max_length=40, default='0')
    view_counts = models.CharField(max_length=50, default='0')

    spam_counts = models.CharField(max_length=40, default=0)  # Spam counts as integer
    branch_counts = models.CharField(max_length=40, default=0)  # Branches companies counts as integer
    product_counts = models.CharField(max_length=40, default=0)  # Product counts as integer
    rating_counts = models.CharField(max_length=40, default=0)  # Rating counts as integer
    active_discount_counts = models.CharField(max_length=40, default=0)  # Active discount counts
    finished_discount_counts = models.CharField(max_length=40, default=0)  # Finished discount counts

    top_tariff_counts = models.CharField(max_length=40, default=0) # Top tariff counts of integer
    boost_tariff_counts = models.CharField(max_length=40, default=0) # Boost tariff counts of integer
    discount_tariff_counts = models.CharField(max_length=40, default=0) # discount tariff counts of integer

    delivery = models.BooleanField(default=False)
    installment = models.BooleanField(default=False)

    short_description = TextField(max_length=2500)
    long_description = TextField(max_length=2500)

    web_site_url = models.URLField(max_length=400, blank=True, null=True)

    longitude = models.FloatField()
    latitude = models.FloatField()

    balance = models.DecimalField(max_digits=30, decimal_places=1, default=0)

    #   Rating fields of Company
    rating5 = models.CharField(max_length=50, default=0)
    rating4 = models.CharField(max_length=50, default=0)
    rating3 = models.CharField(max_length=50, default=0)
    rating2 = models.CharField(max_length=50, default=0)
    rating1 = models.CharField(max_length=50, default=0)

    def get_address(self):
        return {
            'country': self.country,
            'district': self.district,
            'address': self.address,
            'longitude': self.longitude,
            'latitude': self.latitude
        }

    def save(self, *args, **kwargs):
        """
        Generate a unique advertisement ID for new instances before saving
        """
        if self.pk is None:
            self.id_company = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        """
        Generate a unique 8-digit advertisement ID.
        """
        while True:
            # Generate an 8-digit number
            new_id = random.randint(10000000, 99999999)
            # Check for uniqueness
            if not Company.objects.filter(id_company=new_id).exitsts():
                return new_id

    def clean(self):
        if self.district and self.district.split('X')[0] != str(self.region):
            raise ValidationError({'region': 'District and region do not match'})

    def __str__(self):
        return self.name


# @classmethod
# def generate_unique_id(cls, field_name, min_id=10000000, max_id=99999999):
#     while True:
#         new_id = random.randint(min_id, max_id)
#
#         if not cls.objects.filter(field_name=new_id).exists():
#             return new_id