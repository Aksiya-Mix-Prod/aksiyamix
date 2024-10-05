from django.db import models
from django.db.models import IntegerChoices, TextField
from django.core.validators import ValidationError

from src.apps.base.models.base import AbstractBaseModel
from src.apps.categories.models import Category
from src.apps.companies.models import Company, BranchCompany
from src.apps.discounts.choices import Currency, DiscountChoices
from src.apps.features.models import FeatureValue
from src.apps.general.models import CurrencyRate
from src.apps.general.normalize_text import normalize_text
from src.apps.general.validate_file_size import validate_icon_size, validate_image_size


class ServiceDiscount(AbstractBaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    icon = models.ImageField(upload_to='discount/icons/%Y/%m/%d/',
                             validators=[validate_icon_size],
                             blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def get_normalize_fields(self):
        return [
            'name',
            'slug'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Discount(AbstractBaseModel):
    class Status(IntegerChoices):
        PROCESS = 1, 'Process'
        REJECTED = 2, 'Rejected'

    company = models.ForeignKey(Company, on_delete=models.SET_NULL,
                                null=True)
    branch_company = models.ManyToManyField(BranchCompany, related_name='discounts', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 limit_choices_to={"parent__parent_is_null": False})

    status = models.PositiveSmallIntegerField(choices=Status.choices)
    discount_type = models.PositiveSmallIntegerField(choices=DiscountChoices.choices)
    currency = models.PositiveSmallIntegerField(choices=Currency.choices)

    title = models.CharField(max_length=200)

    old_price = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    description = TextField(max_length=2500)

    video = models.FileField(upload_to='discount/videos/%Y/%m/%d/')

    id_generate = models.PositiveIntegerField()
    in_stock = models.PositiveIntegerField()#   nechtadan rasrochka
    available = models.PositiveIntegerField()#  mavjud rasrochka
    views = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

    start_date = models.DateField()
    end_date = models.DateField()

    delivery = models.BooleanField(default=False)
    installment = models.BooleanField(default=False)#   rasrochka
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    #Standart discount
    discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    discount_value_is_percent = models.BooleanField(default=False)

    #Free discount
    min_quantity = models.PositiveIntegerField(blank=True, null=True)
    bonus_quantity = models.PositiveIntegerField(blank=True, null=True)

    #Quantity discount
    bonus_discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    bonus_discount_value_is_percent = models.BooleanField(default=False, blank=True, null=True)

    #Service discount
    service = models.ForeignKey(ServiceDiscount, on_delete=models.SET_NULL, null=True)

    def get_features(self):
        features = {}
        feature_values = FeatureValue.objects.filter(discountfeature__discount__id=self.pk
                                                     ).distinct().select_related('feature')
        for feature_value in feature_values:
            feature = feature_value.feature
            feature_id = features.pk
            feature_name = feature_id.name
            value = {'id': feature_values.id, 'name': feature_value.value}

            if feature_id not in features:
                features[feature_id] = {'name': feature_name, 'values': [value]}
            else:
                features[feature_id]['values'].append(value)

        return features


    def get_old_price_by_currency(self, currency):
        if currency != self.currency:
            return CurrencyRate.objects.get(currency=currency).in_sum * self.old_price
        return self.old_price

    def clean(self):
        """
        Check 4 discount service
        """
        if self.discount_value_is_percent and self.discount_value:
            if not (0 <= self.discount_value <= 100):
                raise ValidationError("Discount must be a percentage between 0 and 100")

        if not self.discount_value_is_percent and self.discount_value:
            if self.currency not in [Currency.USD, Currency.UZS]:
                raise ValidationError("Currency must be USD or UZS")

        if self.discount_type == DiscountChoices.STANDARD:
            if self.discount_value is None:
                raise ValidationError("Standard discount must be required a discount_value")

        elif self.discount_type == DiscountChoices.FREE_PRODUCT:
            if self.min_quantity is None or self.bonus_quantity is None:
                raise ValidationError('Free product discount requires min_quantity and bonus_quantity.')

        elif self.discount_type == DiscountChoices.QUANTITY_DISCOUNT:
            if self.min_quantity is None or self.bonus_discount_value is None:
                raise ValidationError('Quantity discount requires min_quantity and bonus_discount_value.')

        elif self.discount_type == DiscountChoices.SERVICE_DISCOUNT:
            if self.min_quantity is None or self.service is None:
                raise ValidationError('Service discount requires min_quantity and a service.')

    def __str__(self):
        return self.title
