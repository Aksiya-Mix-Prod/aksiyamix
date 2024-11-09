import random

from apps.advertisements.validators.validate_image_size import (
    validate_image_resize_of_advertisements,
    validate_image_size_of_advertisements,
)
from apps.base.exceptions import CustomExceptionError
from apps.base.models import AbstractBaseModel

from django.core.validators import URLValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Advertisement(AbstractBaseModel):
    """
    Advertisement model for products posted by users, managed by admins.
    """

    class PaymentStatusChoices(models.IntegerChoices):
        PENDING = 0, _("Pending")
        PAID = 1, _("Paid")
        DECLINED = 2, _("Declined")

    id_advertisement = models.PositiveSmallIntegerField(unique=True, editable=False)

    title = models.CharField(max_length=200, blank=True, null=True)

    image = models.ImageField(
        upload_to="advertisements/images/%Y/%m/%d/",
        validators=[
            validate_image_resize_of_advertisements,
            validate_image_size_of_advertisements,
        ],
    )
    image2 = models.ImageField(
        upload_to="advertisements/images/%Y/%m/%d/",
        validators=[
            validate_image_resize_of_advertisements,
            validate_image_size_of_advertisements,
        ],
    )
    image3 = models.ImageField(
        upload_to="advertisements/images/%Y/%m/%d/",
        validators=[
            validate_image_resize_of_advertisements,
            validate_image_size_of_advertisements,
        ],
    )

    url_link = models.CharField(max_length=200, validators=[URLValidator()])

    ordering = models.PositiveSmallIntegerField()

    payment_status = models.PositiveSmallIntegerField(
        choices=PaymentStatusChoices.choices,
        blank=True,
        null=True,
        help_text="Status of the payment for the advertisement",
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Indicates if the advertisement is active",
    )

    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        """
        Generate a unique advertisement ID for new instances before saving
        """
        if self.pk is None:
            self.id_advertisement = self.generate_advertisement_id()

        if self.start_date > self.end_date:
            raise CustomExceptionError(
                _(code=400, detail="start_date must be lower than end_date!")
            )

    def generate_advertisement_id(self):
        """
        Generate a unique 8-digit advertisement ID.
        """
        while True:
            # Generate 8-digit number
            new_id = random.randint(1000, 9999)
            # Check for uniqueness
            if not Advertisement.objects.filter(id_advertisement=new_id).exists():
                return new_id

    def __str__(self):
        return self.title
