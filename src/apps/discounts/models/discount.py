from django.db import models
from django.core.validators import MinValueValidator

from apps.services.models import Service
from apps.base.validators.validators import validate_youtube_url
from apps.discounts.utils.unique_id import generate_unique_id
from apps.base.models.base import AbstractBaseModel
from apps.discounts.choices import Currency, DiscountChoices

from apps.base.exceptions import CustomExceptionError
from apps.features.models import FeatureValue


class Discount(AbstractBaseModel):
    class Status(models.IntegerChoices):
        PROCESS = 1, 'Process'
        REJECTED = 2, 'Rejected'
        APPROVED = 3, 'Approved'

    id_generate = models.CharField(
        unique=True,
        max_length=8,
        editable=False,
        default=generate_unique_id
    )
    company = models.ForeignKey(to='companies.Company', on_delete=models.PROTECT,
                                limit_choices_to={
                                    'is_active': True,
                                    'is_deleted': False
                                })
    first_category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.PROTECT,
        related_name='first_category',
    )
    second_category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.PROTECT,
        related_name='second_category',
    )
    category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.PROTECT,
        related_name='discount_category',
        limit_choices_to={
            "parent__parent_is_null": False
        }
    )
    branches = models.ManyToManyField(to='companies.BranchCompany', related_name='discounts', blank=True)

    tags = models.ManyToManyField('tags.Tag', related_name='discounts', blank=True)

    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.PROCESS)
    discount_type = models.PositiveSmallIntegerField(choices=DiscountChoices.choices)
    currency = models.PositiveSmallIntegerField(choices=Currency.choices)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    title = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    old_price = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    description = models.TextField(max_length=2500)

    video_url = models.URLField(validators=[validate_youtube_url], blank=True, null=True)
    image = models.ImageField(upload_to='discount/images/%Y/%m/%d/')

    quantity = models.PositiveIntegerField(help_text='Enter the discount quantity', editable=False, default=0)
    remainder = models.PositiveIntegerField(help_text='Enter the remaining quantity', editable=False, default=0)

    view_counts = models.PositiveIntegerField(default=0)
    like_counts = models.PositiveIntegerField(default=0)
    dislike_counts = models.PositiveIntegerField(default=0)
    comment_counts = models.PositiveIntegerField(default=0)
    spam_counts = models.PositiveIntegerField(default=0)

    start_date = models.DateField()
    end_date = models.DateField()

    delivery = models.BooleanField(default=False)
    installment = models.BooleanField(default=False)

    ordering = models.DateTimeField(auto_now=True)

    # Standard discount
    discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    discount_value_is_percent = models.BooleanField(default=False)

    # Free discount
    min_quantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    free_product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    bonus_quantity = models.PositiveIntegerField(blank=True, null=True)

    # Quantity discount
    # min_quantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    # discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    # discount_value_is_percent = models.BooleanField(default=False)

    # Service discount
    # min_quantity = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)

    def get_features(self):
        features = {}
        feature_values = FeatureValue.objects.filter(discount_feature__discount_id=self.pk).select_related(
            'feature').distinct()

        for value in feature_values:
            if value.feature_id not in features:
                features[value.feature_id] = {
                    'feature_id': value.feature.id,
                    'feature_name': value.feature.name,
                    'values': [
                        {
                            'value_name': value.value,
                            'value_id': value.id,
                        }
                    ]
                }
            else:
                features[value.feature_id]['values'].append(
                    {
                        'value_name': value.value,
                        'value_id': value.id,
                    }
                )

        sorted_features = list(features.values())
        sorted_features.sort(key=lambda obj: len(obj['feature_name']), reverse=True)
        return sorted_features

    def clean(self):
        # Checking the standard deduction

        if self.discount_type == DiscountChoices.STANDARD:
            if self.discount_value is None:
                raise CustomExceptionError(code=400, detail="Standard discount must be required a discount_value")

            if self.discount_value_is_percent and self.discount_value:
                if not (0 <= self.discount_value <= 100):
                    raise CustomExceptionError(code=400, detail="Discount must be a percentage between 0 and 100")

        # Free discount check

        if self.discount_type == DiscountChoices.FREE_PRODUCT:
            if self.min_quantity is None or self.bonus_quantity is None or not self.free_product:
                raise CustomExceptionError(code=400,
                                           detail='Free product discount requires min_quantity, bonus_quantity, and a free product.')

            elif self.bonus_quantity > self.min_quantity:
                raise CustomExceptionError(code=400,
                                           detail='Bonus quantity must be less than or equal to min_quantity.')

            elif self.min_quantity <= 0 or self.bonus_quantity <= 0:
                raise CustomExceptionError(code=400, detail='Min quantity and bonus quantity must be greater than 0.')

        # Quantity discount check

        if self.discount_type == DiscountChoices.QUANTITY_DISCOUNT:
            if self.min_quantity is None:
                raise CustomExceptionError(code=400, detail='Quantity discount requires a min_quantity')

            if self.discount_value_is_percent and self.discount_value:
                if not (0 <= self.discount_value <= 100):
                    raise CustomExceptionError(code=400, detail="Discount must be a percentage between 0 and 100")

        # Service discount check
        if self.discount_type == DiscountChoices.SERVICE_DISCOUNT:
            if self.service is None:
                raise CustomExceptionError(
                    code=400,
                    detail='Service discount requires a valid service.'
                )

            if self.min_quantity is None:
                raise CustomExceptionError(
                    code=400,
                    detail='Service discount requires a min_quantity.'
                )

    def save(self, *args, **kwargs):
        if self.category and self.category.parent:
            self.second_category = self.category.parent
            if self.category.parent.parent:
                self.first_category = self.category.parent.parent

        super().save(*args, **kwargs)


def __str__(self):
    return self.title
