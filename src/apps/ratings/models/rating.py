from django.db import models
from django.conf import settings


class Rating(models.Model):
    """
    Rating Model
    """

    company = models.ForeignKey(
        to='companies.Company',
        on_delete=models.CASCADE,
        help_text='which company to rate',
        limit_choices_to={'is_active': True, 'is_verified': True, 'is_deleted': False},
    )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        help_text='which user is rating',
        limit_choices_to={'is_active': True, 'is_spam': False},
    )

    rating_value = models.PositiveSmallIntegerField(help_text='rating of user', editable=False)

    class Meta:
        db_table = "rating"
        unique_together = (('company', 'user'),)

