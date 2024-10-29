from decimal import Decimal
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from django.utils import timezone
from apps.payments.models import Order, Transaction
from apps.payments.utils.payme_errors import PaymeErrorResponse
from apps.base.views.viewsets import CustomGenericViewSet
from apps.payments.permissions import PaymePermission, IsAdminOrIsCompanyOwner
from apps.payments.serializers import OrderSerializer, TransactionSerializer




class PaymeGenericViewSet(CustomGenericViewSet, PaymeErrorResponse):
    """
    API for handling Payme merchant API endpoints.
    Implements all required methods for payment processing except Payme Initialization

    Complete Flow Example for Client developers:
        1. User clicks "Pay" in our app
        2. Client calls your PaymentInitializationViewSet (look for it in comments of APIs)
        3. Server creates order and returns Payme params
        4. Client redirects to Payme with these params
        5. User completes payment on Payme
        6. Payme calls our PaymeGenericViewSet endpoints to verify/process payment
        7. Payment completes, order status updates --> (Client can use PerformTransaction handler
                or  make periodic checkups on CheckTransaction handler to see if the payments is done.)
    """
    permission_classes = [IsAuthenticated, IsAdminOrIsCompanyOwner, PaymePermission]
    serializer_class = [OrderSerializer, TransactionSerializer]


    @action(detail=False, methods=['post'])
    def check_perform_transaction(self, request):
        """
        CheckPerformTransaction handler
        Validates if a transaction can be performed for a given order
        """
        global request_id
        try:
            data = request.data
            request_id = data.get('id', 0)
            params = data.get('params', {})

            amount = params.get('amount')
            order_id = params.get('account', {}).get('order_id')

            if not order_id:
                return self.get_error_response('order_not_found', request_id)

            try:
                order = Order.objects.get(_id=order_id)
            except Order.DoesNotExist:
                return self.get_error_response('order_not_found', request_id)

            if order.is_paid:
                return self.get_error_response('order_already_paid', request_id)

            amount_in_sum = Decimal(amount) / 100
            if amount_in_sum != order.amount:
                return self.get_error_response('incorrect_amount', request_id)

            return self.get_success_response({"allow":True}, request_id)

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)


    @action(detail=False, methods=['post'])
    def create_transaction(self, request):
        """
        CreateTransaction handler
        Creates a new transaction for the order
        """
        global request_id
        try:
            data = request.data
            request_id = data.get('id', 0)
            params = data.get('params', {})

            transaction_id = params.get('id')
            time = params.get('time')
            amount = params.get('amount')
            order_id = params.get('account', {}).get('order_id')

            if not all([transaction_id, time, amount, order_id]):
                return self.get_error_response('unable_to_perform', request_id)

            try:
                order = Order.objects.get(_id=order_id)
            except Order.DoesNotExist:
                return self.get_error_response('order_not_found', request_id)

            existing_transaction = Transaction.objects.filter(
                order=order,
                payment_system='Payme',
            ).first()

            if existing_transaction:
                return self.get_success_response({
                    "create_time": int(existing_transaction.date_time.timestamp() * 1000),
                    "transaction": str(existing_transaction.id),
                    "state": 1 if not existing_transaction.state else 2,
                }, request_id)

            transaction = Transaction.objects.create(
                order=order,
                payment_system='Payme',
                amount=Decimal(amount) / 100,
                status=False
            )

            return self.get_success_response({
                "create_time": int(transaction.date_time.timestamp() * 1000),
                "transaction": str(transaction.id),
                "state": 1
            }, request_id)

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)


    @action(detail=False, methods=['post'])
    def perform_transaction(self, request):
        """
        PerformTransaction handler
        Completes the transaction and updates order status
        """
        global request_id
        try:
            data = request.data
            request_id = data.get('id', 0)
            params = data.get('params', {})

            transaction_id = params.get('id')

            try:
                transaction = Transaction.objects.get(_id=transaction_id)
            except Transaction.DoesNotExist:
                return self.get_error_response('transaction_not_found', request_id)

            if transaction.status:
                return self.get_success_response({
                    "perform_time":int(transaction.date_time.timestamp() * 1000),
                    "transaction": str(transaction.id),
                    "state": 2
                }, request_id)

            transaction.status = True
            transaction.save()

            if transaction.order:
                transaction.order.is_paid = True
                transaction.order.save()

            return self.get_success_response({
                "perform_time": int(timezone.now().timestamp() * 1000),
                "transaction": str(transaction.id),
                "state": 2
            }, request_id)

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)


    @action(detail=False, methods=['post'])
    def cancel_transaction(self, request):
        """
        CancelTransaction handler
        Cancels the transaction and updates the order status
        """
        global request_id
        try:
            data = request.data
            request_id = data.get('id', 0)
            params = data.get('params', {})

            transaction_id = params.get('id')

            try:
                transaction = Transaction.objects.get(_id=transaction_id)
            except Transaction.DoesNotExist:
                return self.get_error_response('transaction_not_found', request_id)

            if transaction.order:
                transaction.order.is_paid = False
                transaction.order.save()

            return self.get_success_response({
                "cancel_time": int(timezone.now().timestamp() * 1000),
                "transaction": str(transaction.id),
                "state": -1
            }, request_id)

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)


    @action(detail=False, methods=['post'])
    def check_transaction(self, request):
        """
        CheckTransaction handler
        Checks the current state of a transaction
        """
        global request_id
        try:
            data = request.data
            request_id = data.get('id', 0)
            params = data.get('params', {})

            transaction_id = params.get('id')

            try:
                transaction = Transaction.objects.get(_id=transaction_id)
            except Transaction.DoesNotExist:
                return self.get_error_response('transaction_not_found', request_id)

            response_data = {
                "create_time": int(transaction.date_time.timestamp() * 1000),
                "perform_time": int(timezone.datetime.timestamp() * 1000) if transaction.status else 0,
                "cancel_time": 0,
                "transaction": str(transaction.id),
                "state": 2 if transaction.status else 1,
                "reason": None
            }

            return self.get_success_response(response_data, request_id)

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)


    @action(detail=False, methods=['post'])
    def get_statement(self, request):
        """
        GetStatement handler
        Returns the transaction history for a given period
        """
        global request_id
        try:
            data = request.data
            request_id = data.get('id', 0)
            params = data.get('params', {})

            from_date = timezone.datetime.fromtimestamp(params.get('from') / 1000)
            to_date = timezone.datetime.fromtimestamp(params.get('to') / 1000)

            transactions = Transaction.objects.filter(
                date_time__gte=from_date,
                date_time__lte=to_date,
                payment_system='Payme',
            )

            response_date = {
                "transactions": [
                    {
                        "id": str(t.id),
                        "time": int(t.date_time.timestamp() * 1000),
                        "amount": int(t.amount * 100),
                        "account": {
                            "order_id": t.order._id if t.order else None,
                        },
                        "create_time": int(t.date_time.timestamp() * 1000),
                        "perform_time": int(t.date_time.timestamp() * 1000) if t.status else 0,
                        "cancel_time": 0,
                        "transaction": str(t.id),
                        "state": 2 if t.status else 1,
                        "reason": None
                    } for t in transactions
                ]
            }

            return self.get_success_response(response_date, request_id)

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)









