from django.db import models
from django.db.models import IntegerChoices, TextField
from django.core.validators import ValidationError

from src.apps.base.models.base import AbstractBaseModel
from src.apps.categories.models import Category
from src.apps.companies.models import Company, BranchCompany
from src.apps.discounts.choices import Currency, DiscountChoices
from src.apps.services.models import Service
from src.apps.likes.models import DiscountLike, DiscountDislike
from src.apps.comments.models import Comment


class Discount(AbstractBaseModel):
    class Status(IntegerChoices):
        PROCESS = 1, 'Process'
        REJECTED = 2, 'Rejected'
        APPROVED = 3, 'Approved'

    id = models.PositiveSmallIntegerField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,
                                null=True)
    first_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    second_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 limit_choices_to={"parent__parent_is_null": False})
    branch_company = models.ManyToManyField(BranchCompany, related_name='discounts', blank=True)

    tags = models.ManyToManyField('tags.Tag',  related_name='discounts', blank=True)

    status = models.PositiveSmallIntegerField(choices=Status.choices,  default=Status.PROCESS)
    discount_type = models.PositiveSmallIntegerField(choices=DiscountChoices.choices)
    currency = models.PositiveSmallIntegerField(choices=Currency.choices)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    title = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    old_price = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    description = TextField(max_length=2500)

    video_url = models.URLField(upload_to='discount/videos/%Y/%m/%d/')
    image =  models.ImageField(upload_to='discount/images/%Y/%m/%d/')

    quantity = models.PositiveIntegerField(help_text='Enter the discount quantity')#   nechtadan rasrochka
    remainder = models.PositiveIntegerField(help_text='Enter the remaining quantity')#  mavjud rasrochka

    view_counts = models.PositiveIntegerField()
    like_counts = models.PositiveIntegerField()
    dislike_counts = models.PositiveIntegerField()
    comment_counts = models.PositiveIntegerField()
    spam_counts = models.PositiveIntegerField()

    start_date = models.DateField()
    end_date = models.DateField()

    delivery = models.BooleanField(default=False)
    installment = models.BooleanField(default=False)

    ordering = models.DateTimeField(auto_now=True)

    #Standart discount
    discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    discount_value_is_percent = models.BooleanField(default=False)

    #Free discount
    min_quantity = models.PositiveIntegerField(blank=True, null=True)
    free_product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True)
    bonus_quantity = models.PositiveIntegerField(blank=True, null=True)

    #Quantity discount
    # min_quantity = models.PositiveIntegerField(blank=True, null=True)
    # discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    # discount_value_is_percent = models.BooleanField(default=False)

    #Service discount
    # min_quantity = models.PositiveIntegerField(blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)


    def clean(self):

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
            if self.service is None:
                raise ValidationError('Service discount requires a service.')

    def save(self, *args, **kwargs):
        if self.category and self.category.parent:
            self.second_category = self.category.parent
            if self.category.parent.parent:
                self.first_category = self.category.parent.parent

        like_counts = DiscountLike.objects.filter(discount=self).count()
        dislike_counts = DiscountDislike.objects.filter(discount=self).count()
        comment_counts = Comment.objects.filter(discount=self).count()

        self.like_counts = like_counts
        self.dislike_counts = dislike_counts
        self.comment_counts = comment_counts
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
