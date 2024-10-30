from django.conf import settings
from django.db import models

from apps.base.models.base import AbstractBaseModel
from apps.complaints.choice.compalint_type import ComplaintType


class Complaint(AbstractBaseModel):
    """
    Here creating complaint of users
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True,
                             limit_choices_to={
                                 'is_active': True,
                                 'is_spam': False,
                             })

    discount = models.ForeignKey('discounts.Discount',
                                 on_delete=models.SET_NULL,
                                 null=True)

    comment = models.ForeignKey('comments.Comment',
                                on_delete=models.SET_NULL,
                                null=True)

    company = models.ForeignKey('companies.Company', on_delete=models.SET_NULL,
                                blank=True, null=True)

    complaint_types = models.PositiveSmallIntegerField(choices=ComplaintType.choices,
                                                       default=ComplaintType.NAME_OF_COMPANY)

    message = models.CharField(max_length=200)
    first_name = models.CharField(max_length=255)

    viewed = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'discount'], name='unique_user_discount'),
            models.UniqueConstraint(fields=['user', 'company'], name='unique_user_company')
        ]


    def __str__(self):
        return self.first_name
