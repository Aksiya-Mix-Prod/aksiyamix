from django.db import models
from django.core.validators import MinValueValidator


class General(models.Model):
    """
    Model to general items or details of the web-site.
    """

    # howmuch is one usd in one uzs
    one_usd_in_uzs = models.DecimalField(
        max_length=5,
        max_digits=2,
        validators=[MinValueValidator(0)],
        decimal_places=2
    )

    # date when usd value for uzs updated
    date = models.DateField(auto_now_add=True)

    # minimum amount of company balance replenishment
    min_order_amount = models.CharField(max_length=100)

    # maximum amount of company balance replenishment
    max_order_amount = models.CharField(max_length=100)

    class Meta:
        db_table = "general"
    
