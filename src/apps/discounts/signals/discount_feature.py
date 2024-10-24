from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.discounts.models import DiscountFeature


@receiver(post_save, sender=DiscountFeature)
def update_discount_price(sender, instance, created, **kwargs):
    if created and instance.discount.discount_features.count() == 1:
        instance.discount.price = instance.price
        instance.discount.old_price = instance.old_price
        instance.discount.save()
