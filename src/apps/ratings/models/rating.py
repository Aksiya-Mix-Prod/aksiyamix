from django.conf import settings
from django.db import models

from apps.base.exceptions import CustomExceptionError
from apps.base.models import AbstractBaseModel


class Rating(AbstractBaseModel):
    """
    Rating Model
    """

    company = models.ForeignKey(
        to='companies.Company',
        on_delete=models.CASCADE,
        limit_choices_to={'is_active': True, 'is_verified': True, 'is_deleted': False},
        help_text='which company to rate'
    )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'is_active': True, 'is_spam': False},
        help_text='which user is rating'
    )

    rating_value = models.PositiveSmallIntegerField(editable=False, help_text='rating of user')

    def clean(self, *args, **kwargs):
        if self.rating_value < 1 or self.rating_value > 5:
            raise CustomExceptionError(
                code=400,
                detail={"rating_value": "Rating value should be more than 1 and less than 5"}
            )


    class Meta:
        db_table = "rating"
        unique_together = (('company', 'user'),)


