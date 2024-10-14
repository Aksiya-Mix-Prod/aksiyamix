from django.db.models import IntegerChoices


class Currency(IntegerChoices):
    UZS = 1, 'Uzs',
    USD = 2, 'Usd'


class DiscountChoices(IntegerChoices):
    STANDARD = 1, 'Standard'
    FREE_PRODUCT = 2, 'Free Product'
    QUANTITY_DISCOUNT = 3, 'Quantity Discount'
    SERVICE_DISCOUNT = 4, 'Service Discount'