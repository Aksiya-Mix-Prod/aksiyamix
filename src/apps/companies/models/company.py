from django.conf import settings
from django.db import models
from django.db.models import TextField
from django.core.validators import FileExtensionValidator
from django.core.validators import ValidationError

from src.apps.categories.models.category import Category
from src.apps.users.validators.phone_number import phone_validate
from src.apps.base.models.base import AbstractBaseModel
from src.apps.companies.choice.country import Country
from src.apps.companies.choice.disctrict import District

from src.apps.companies.validators.company_video_size import validate_company_video_size
from src.apps.companies.validators.company_logo_size import (validate_company_logo_size, validate_logo_size)
from src.apps.companies.validators.company_banner_size import validate_company_banner_size, validate_banner_size


class Company(AbstractBaseModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category, blank=True, related_name='companies')

    #   BIO FOR CREATE COMPANY ------ Here create of Owner

    owner_last_name = models.CharField(max_length=120)
    owner_first_name = models.CharField(max_length=120)
    owner_father_name = models.CharField(max_length=120)
    owner_phone_number1 = models.CharField(max_length=13, validators=[phone_validate])
    owner_phone_number2 = models.CharField(max_length=13, validators=[phone_validate])

    #   CREATE COMPANY ------- Here files of Company

    logo = models.ImageField(upload_to='company/logos/%Y/%m/%d/',
                             validators=[validate_company_logo_size,
                                         validate_logo_size],
                             blank=True, null=True)

    video_url = models.FileField(upload_to='company/videos/%Y/%m/%d/',
                                 validators=[
                                     FileExtensionValidator(allowed_extensions=['mp4']),
                                     validate_company_video_size],
                                 blank=True, null=True)

    banner = models.ImageField(upload_to='company/banners/%Y/%m/%d/',
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

    id_generate = models.CharField(max_length=40, default='0')
    follower_counts = models.CharField(max_length=40, default='0')
    like_counts = models.CharField(max_length=40, default='0')
    dislike_counts = models.CharField(max_length=40, default='0')
    comment_counts = models.CharField(max_length=40, default='0')
    view_counts = models.CharField(max_length=50, default='0')
    spam_counts = models.PositiveSmallIntegerField(max_length=40,
                                                   default=0)  # Spam counts as integer
    branch_counts = models.PositiveSmallIntegerField(max_length=40,
                                                     default=0)  # Branches companies counts as integer
    product_counts = models.PositiveSmallIntegerField(max_length=40,
                                                     default=0)  # Product counts as integer
    rating_counts = models.PositiveSmallIntegerField(max_length=40,
                                                     default=0)  # Rating counts as integer
    active_discount_counts = models.PositiveSmallIntegerField(max_length=40,
                                                     default=0)  # Active discount counts
    finished_discount_counts = models.PositiveSmallIntegerField(max_length=40,
                                                     default=0)  # Finished discount counts

    top_tariff_counts = models.PositiveSmallIntegerField(max_length=40, default=0)
    boost_tariff_counts = models.PositiveSmallIntegerField(max_length=40, default=0)
    discount_tariff_counts = models.PositiveSmallIntegerField(max_length=40, default=0)

    delivery = models.BooleanField(default=False)
    installment = models.BooleanField(default=False)

    short_description = TextField(max_length=2500)
    long_description = TextField(max_length=2500)

    web_site_url = models.URLField(max_length=300, blank=True, null=True)

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

    def clean(self):
        if self.district and self.district.split('X')[0] != str(self.region):
            raise ValidationError({'region': 'District and region do not match'})

    def __str__(self):
        return self.name
