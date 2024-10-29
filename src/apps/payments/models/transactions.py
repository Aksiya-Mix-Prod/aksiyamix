from django.db import models
from apps.base.models import AbstractBaseModel
from apps.payments.utils.unique_id import generate_unique_id


class Transaction(AbstractBaseModel):
    """
    Transaction model for recording payment transactions.

    This model represents individual payment transactions in the system. It is
    associated with a specific Order and tracks details such as the payment system used,
    transaction status, amount, and any error messages.

    Attributes:
        order (ForeignKey): Reference to the Order model. Set to NULL if the order is deleted.
        payment_system (CharField): The payment system used for the transaction.
            Choices are 'Payme', 'Uzum', or 'Click'.
        date_time (DateTimeField): Timestamp of when the transaction was created.
        status (BooleanField): Indicates whether the transaction was successful (True) or not (False).
        error_message (CharField): Optional field to store any error message if the transaction fails.
        amount (DecimalField): The monetary amount of the transaction.

    Usage:
        This model is used to keep a detailed record of all payment transactions,
        providing a comprehensive view of the payment history for each order.
    """

    PAYMENT_SYSTEM_CHOICES = (
        ('Payme', 'Payme'),
        ('Uzum', 'Uzum'),
        ('Click', 'Click'),
    )

    order = models.ForeignKey(
        to='payments.Order',
        on_delete=models.SET_NULL,
        related_name='transactions',
        null=True,
    )
    _id = models.CharField(max_length=10, default=generate_unique_id, editable=False)
    payment_system = models.CharField(choices=PAYMENT_SYSTEM_CHOICES, max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    error_message = models.CharField(blank=True, max_length=100, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        ordering = ['-date_time']
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f"{self.date_time} - {self.payment_system} - {self.amount}"