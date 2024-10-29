import random

from django.db import models
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _

from apps.base.models import AbstractBaseModel
from apps.base.exceptions import CustomExceptionError


class Advertisement(AbstractBaseModel):
    """
    Here creating Advertisement model of Companies
    """

    id_advertisement = models.PositiveSmallIntegerField(unique=True, editable=False)
    title = models.CharField(max_length=200, blank=True, null=True)

    image = models.ImageField(upload_to='advertisements/images/%Y/%m/%d/')

    url_link = models.CharField(max_length=200,
                                validators=[URLValidator()]
                                )

    ordering = models.PositiveSmallIntegerField()

    start_date = models.DateField()
    end_date = models.DateField()


    def clean(self):
        """
        Generate a unique advertisement ID for new instances before saving
        """
        if self.pk is None:
            self.id_advertisement = self.generate_advertisement_id()

        if self.start_date > self.end_date:
            raise CustomExceptionError(_(code=400, detail='start_date must be lower that end_date!!!'))

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
