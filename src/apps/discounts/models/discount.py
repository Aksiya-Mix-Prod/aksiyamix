from django.core.validators import MinValueValidator
from django.db import models

from apps.base.models.base import AbstractBaseModel
from apps.base.validators.validators import validate_youtube_url
from apps.discounts.choices import Currency, DiscountChoices
from apps.discounts.utils.unique_id import generate_unique_id
from apps.discounts.validators import discount
from apps.features.models import FeatureValue
from apps.services.models import Service


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
            "parent__parent__isnull": False
        }
    )
    branches = models.ManyToManyField(to='branches.BranchCompany', related_name='discounts', blank=True)

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
        discount.validate_standard_discount(self)
        discount.validate_free_product_discount(self)
        discount.validate_quantity_discount(self)
        discount.validate_service_discount(self)


    def save(self, *args, **kwargs):
        if self.category and self.category.parent:
            self.second_category = self.category.parent
            if self.category.parent.parent:
                self.first_category = self.category.parent.parent

        super().save(*args, **kwargs)


def __str__(self):
    return self.title
