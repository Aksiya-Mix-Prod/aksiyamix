from venv import create

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from ..models.rating import Rating
from apps.companies.models.company import Company

@receiver(post_save, sender=Rating)
def update_company_rating(sender, instance, created, **kwargs):
    rating_value = instance.rating_value
    company = instance.company

    if created:
        field_name = f'rating{rating_value}'
        rating = int(getattr(company, field_name))
        rating += 1
        setattr(company, field_name, str(rating))
        company.save()


@receiver(post_delete, sender=Rating)
def update_company_rating_on_delete(sender, instance, **kwargs):
    rating_value = instance.rating_value
    company = instance.company

    field_name = f'rating{rating_value}'
    rating = int(getattr(company, field_name))
    rating -= 1
    print('444', type(rating))
    setattr(company, field_name, str(rating))
    company.save()

