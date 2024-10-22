import string
import random
from django.db import models
from apps.base.models import AbstractBaseModel

def generate_unique_id():
    """ Generate a unique id for the Order model """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(8))


class Order(AbstractBaseModel):
    """
    Order model for handling payment orders.

    This model represents a payment order in the system. It uses a unique
    8-character ID and is closely associated with the Transaction model.

    Attributes:
        id (CharField): Unique 8-character identifier for the order.
        company (ForeignKey): Reference to the Company model.
        amount (DecimalField): The monetary amount of the order.
        is_paid (BooleanField): Indicates whether the order has been paid.

    Usage:
        This model is typically used in conjunction with the Transaction model
        to track payment orders and their associated transactions.
    """
    # ======== Generate unique 8 char IDs for each Order ========
    id = models.CharField(primary_key=True, max_length=8, default=generate_unique_id, editable=False)
    company = models.ForeignKey(to='companies.Company', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order {self.id} - {self.company} - {self.amount}"