from django.conf import settings
from django.db import models
from django.db.models import TextField
from django.core.validators import FileExtensionValidator

from src.apps.categories.models.category import Category
from src.apps.base.models.base import AbstractBaseModel
from src.apps.companies.choice.country import Country
from src.apps.companies.choice.disctrict import District

from src.apps.companies.validators.company_video_size import validate_company_video_size
from src.apps.companies.validators.company_logo_size import (validate_company_logo_size, validate_logo_size,
                                                             validate_icon_size)
from src.apps.companies.validators.company_banner_size import validate_company_banner_size, validate_banner_size


class Company(AbstractBaseModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category, blank=True, related_name='companies')

    #   BIO FOR CREATE COMPANY ------ Here create of Owner

    last_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120)

    #   CREATE COMPANY ------- Here files of Company

    logo = models.ImageField(upload_to='company/logos/%Y/%m/%d/',
                             validators=[validate_company_logo_size,
                                         validate_logo_size],
                             blank=True, null=True)

    icon = models.ImageField(upload_to='company/icons/%Y/%m/%d/',
                             validators=[validate_icon_size],
                             blank=True, null=True)

    video = models.FileField(upload_to='company/videos/%Y/%m/%d/',
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
    slogan = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])

    id_generate = models.CharField(max_length=40, default='0')
    followers = models.CharField(max_length=40, default='0')
    likes = models.CharField(max_length=40, default='0')
    comments = models.CharField(max_length=40, default='0')
    views = models.CharField(max_length=50, default='0')

    delivery = models.BooleanField(default=False)
    installment = models.BooleanField(default=False)

    description = TextField(max_length=2500)

    web_site = models.URLField(max_length=300, blank=True, null=True)

    longitude = models.FloatField()
    latitude = models.FloatField()

    balance = models.DecimalField(max_digits=30, decimal_places=1, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

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
        cleaned_data = super().clean()
        country = cleaned_data.get('country')
        district = cleaned_data.get('district')

        # Define valid districts for each country
        country_districts = {
            Country.TASHKENT: [
                District.TASHKENT_CITY,
                District.YUNUSABAD,
                District.MIRABAD,
                District.CHILANZAR,
            ],
            Country.FERGANA: [
                District.FERGANA_CITY,
                District.KUVA,
                District.RISHTAN,
            ],
            Country.SAMARKAND: [
                District.SAMARKAND_CITY,
                District.URGUT,
                District.KATTALIK,
            ],
            Country.BUKHARA: [
                District.BUKHARA_CITY,
                District.JONDOR,
                District.GIDRO,
            ],
            Country.ANDIJAN: [
                District.ANDIJAN_CITY,
                District.ASAKA,
                District.KURGANTEPA,
            ],
            Country.NAVOI: [
                District.NAVOI_CITY,
                District.ZARAFSHAN,
                District.UCHKUDUK,
            ],
            Country.QARSHI: [
                District.QARSHI,
                District.KOSON,
                District.SHAKHRISABZ,
            ],
            Country.JIZZAKH: [
                District.JIZZAKH_CITY,
                District.PASTDARGOM,
                District.FORISH,
            ],
            Country.KHOREZM: [
                District.URGENCH,
                District.KHIVA,
                District.YANGIYER,
            ],
            Country.KOKAND: [
                District.KOKAND_CITY,
                District.RUSTAMYON,
                District.FAYZABAD,
            ],
            Country.TERMEZ: [
                District.TERMEZ_CITY,
                District.BOYSUN,
                District.SHERABAD,
            ],
        }

        if country in country_districts and district not in country_districts[country]:
            self.add_error('district', 'Selected district is not valid for the chosen country.')
        return cleaned_data


    def __str__(self):
        return self.name