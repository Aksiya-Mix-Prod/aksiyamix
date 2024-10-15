from django.db import models
from django.core.validators import URLValidator

from src.apps.advertisements.validators import validate_image_size


class Advertisement(models.Model):
    """
    Here creating Advertisement model of Companies
    """
    title = models.CharField(max_length=200, blank=True, null=True)

    image = models.ImageField(upload_to='advertisement/images/%Y/%m/%d/',
                              validators=[validate_image_size])

    url_link = models.CharField(max_length=200,
                                validators=[URLValidator()]
                                )

    ordering = models.PositiveSmallIntegerField()

    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        constraint = [
            models.UniqueConstraint(fields=['category', 'discount'], name='unique_category_discount')
        ]

    def __str__(self):
        return self.title
