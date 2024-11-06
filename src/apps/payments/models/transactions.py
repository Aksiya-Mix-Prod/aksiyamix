from django.db import models
from apps.base.models import AbstractBaseModel
from apps.payments.utils.unique_id import generate_unique_id
from django.utils import timezone


class Transaction(AbstractBaseModel):
    """
    Transaction model for recording payment transactions.

    Attributes:
        order (ForeignKey): Reference to the Order model.
        payment_system (CharField): The payment system used for the transaction.
        date_time (DateTimeField): Timestamp of when the transaction was created.
        status (BooleanField): Indicates whether the transaction was successful (True) or not (False).
        error_message (CharField): Optional field to store any error message if the transaction fails.
        amount (DecimalField): The monetary amount of the transaction.
        payme_transaction_id (CharField): The transaction ID provided by Payme.
        perform_time (DateTimeField): Timestamp when the transaction was performed.
        cancel_time (DateTimeField): Timestamp when the transaction was canceled.
        reason (IntegerField): Reason code for cancellation, if applicable.
        state (IntegerField): Current state of the transaction as per Payme's specification.
    """

    PAYMENT_SYSTEM_CHOICES = (('Payme', 'Payme'), ('Uzum', 'Uzum'), ('Click', 'Click'),)

    order = models.ForeignKey(
        to='payments.Order', on_delete=models.SET_NULL, related_name='transactions', null=True, )
    _id = models.CharField(max_length=10, default=generate_unique_id, editable=False)
    payment_system = models.CharField(choices=PAYMENT_SYSTEM_CHOICES, max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    error_message = models.CharField(blank=True, max_length=100, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20)

    # ========= New fields added for Payme integration =========
    payme_transaction_id = models.CharField(max_length=64, unique=True, null=True, blank=True)
    perform_time = models.DateTimeField(null=True, blank=True)
    cancel_time = models.DateTimeField(null=True, blank=True)
    reason = models.IntegerField(null=True, blank=True)

    # ==== State as per Payme's specification (e.g., 1 for pending, 2 for completed, -1 or -2 for canceled). =====
    state = models.IntegerField(default=1)

    class Meta:
        ordering = ['-date_time']
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f"{self.date_time} - {self.payment_system} - {self.amount}"
