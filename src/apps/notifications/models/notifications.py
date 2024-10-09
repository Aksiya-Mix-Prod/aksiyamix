from django.db import models

from apps.base.models import AbstractBaseModel


class Notification(AbstractBaseModel):
    class Type(models.IntegerChoices):
        NEWS = 0, 'News'
        FOLLOW = 1, 'Follow'
        DISCOUNT = 2, 'Created Discount'
        COMMENT = 3, 'Comment'
        COMPLAINT = 4, 'Complaint'
        SPAM = 5, 'Spam'
        PAYMENT = 6, 'Payment'
        ADVERTISING = 7, 'Advertising'
        OTHER = 8, 'Other'

    notification_type = models.PositiveIntegerField(max_length=50, choices=Type.choices)

    company = models.ForeignKey("companies.Company", on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='notification/images/%Y/%m/%d', blank=True, null=True)
    message = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notification'

    def __str__(self):
        return self.title