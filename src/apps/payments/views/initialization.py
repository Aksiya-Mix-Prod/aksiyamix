from kombu.asynchronous.http import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.base.views.viewsets import CustomGenericViewSet
from apps.payments.models import Order
from apps.payments.permissions import IsAdminOrIsCompanyOwner
from apps.payments.views.payment_url import GeneratePayLink


class PaymeInitGenericViewSet(CustomGenericViewSet):
    """
    API for handling Payme merchant API Initialization.
    Implements all required methods for Payme Initialization

    Payment initialization happens every time a user starts a new payment flow
        The initialization:
            - Creates a new unpaid order
            - Generates the necessary Payme parameters (merchant ID, amount in tiyin, etc.)
            - Provides the frontend with data needed to redirect to Payme's payment page
    """
    # serializer_class = PaymentInitSerializer # don't serialize anything from Payme
    permission_classes = [IsAuthenticated, IsAdminOrIsCompanyOwner]

    def create(self, request):
        # ======== Create an unpaid order ========
        order = Order.objects.create(
            user=request.user,
            amount=request.data['amount'],
            is_paid=False
        )
        url = GeneratePayLink(
            order_id=order.id,
            amount=order.amount
        ).generate_link()

        # ======== Serialize order with Payme data ========
        serializer = self.get_serializer(order)

        # ======== Return the data needed for frontend to redirect to Payme ========
        # data = serializer.data
        # data.update(url=url)
        return Response({
            'url': url,
        }, code=status.HTTP_201_CREATED)


