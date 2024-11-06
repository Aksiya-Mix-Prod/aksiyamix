from decimal import Decimal

from django.utils import timezone
from apps.payments.models import Order, Transaction
from apps.payments.utils.payme_errors import PaymeErrorResponse
from apps.base.views.generics import CustomGenericAPIView
from apps.payments.permissions import PaymeAuthPermission
from apps.payments.serializers import OrderSerializer, TransactionSerializer



class PaymeGenericAPIView(CustomGenericAPIView, PaymeErrorResponse):
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
    permission_classes = [PaymeAuthPermission]
    serializer_class = [OrderSerializer, TransactionSerializer]

    def post(self, request, *args, **kwargs):
        method = request.data['method']
        if method == 'CheckPerformTransaction':
            return self.check_perform_transaction(request)
        elif method == 'CreateTransaction':
            return self.create_transaction(request)
        elif method == 'PerformTransaction':
            return self.perform_transaction(request)
        elif method == 'CancelTransaction':
            return self.cancel_transaction(request)
        elif method == 'CheckTransaction':
            return self.check_transaction(request)
        elif method == 'GetStatement':
            return self.get_statement(request)


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
            print(F"Amount from payme: {amount}")
            order_id = params.get('account', {}).get('order_id')

            if not order_id:
                return self.get_error_response('order_not_found', request_id)

            try:
                order = Order.objects.get(_id=order_id)
            except Order.DoesNotExist:
                return self.get_error_response('order_not_found', request_id)

            if order.is_paid:
                return self.get_error_response('order_already_paid', request_id)

            # print(f"Amount from admin: {amount_in_sum}")
            print(f"Order amount: {order.amount}")
            if amount != int(order.amount):
                error =  self.get_error_response('invalid_amount', request_id)
                print(error)
                return error


            return self.get_success_response({'allow':True}, request_id)

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)


    def create_transaction(self, request):
        """
        CreateTransaction handler
        Creates a new transaction for the order
        """
        global request_id
        # try:
        data = request.data
        request_id = data.get('id', 0)
        params = data.get('params', {})

        payme_transaction_id = params.get('id')
        time = params.get('time')
        amount = params.get('amount')
        order_id = params.get('account', {}).get('order_id')

        if not all([payme_transaction_id, time, amount, order_id]):
            return self.get_error_response('unable_to_perform', request_id)

        # ======== Fetch the Order ========
        try:
            order = Order.objects.get(_id=order_id)
        except Order.DoesNotExist:
            return self.get_error_response('order_not_found', request_id)

        # ======== Validate the amount ========
        if amount != int(order.amount):
            return self.get_error_response('invalid_amount', request_id)

        # ========= Check if transaction with Payme transaction ID already exists ========
        try:
            transaction = Transaction.objects.get(payme_transaction_id=payme_transaction_id)
            # ==== Check if the transaction matches the params ====
            if transaction.amount != Decimal(amount/100) or transaction.order != order:
                return self.get_error_response('transaction_cannot_perform', request_id)
            # ==== return the existing transaction ====
            state = 1 if not transaction.status else 2
            return self.get_success_response(
                {
                    "create_time": int(transaction.date_time.timestamp() * 1000),
                    "transaction": payme_transaction_id,
                    "state": state,
                },
                request_id
            )
        except Transaction.DoesNotExist:
            pass # ========= it means no existing transaction with this Payme transaction ID =========

        # ========= Check if there's another transaction in progress for this order ========
        existing_transaction = Transaction.objects.filter(
            order=order, payment_system='Payme', status=False
        ).exclude(payme_transaction_id=payme_transaction_id).first()

        if existing_transaction:
            # ========= Return error if another transaction is in progress =========
            return self.get_error_response('another_transaction_in_progress', request_id)

        # ========= Create a new transaction ========
        transaction = Transaction.objects.create(
            payme_transaction_id=payme_transaction_id,
            order=order,
            payment_system='Payme',
            amount=Decimal(amount/100), # ==== Convert amount from tiyin to sum ====
            status=False
        )

        return self.get_success_response(
            {
                "create_time":int(transaction.date_time.timestamp() * 1000),
                "transaction":payme_transaction_id,
                "state":1
            },
            request_id
        )


    def perform_transaction(self, request):
        """
        PerformTransaction handler
        Completes the transaction and updates order status
        """
        global request_id
        data = request.data
        request_id = data.get('id', 0)
        params = data.get('params', {})
        payme_transaction_id = params.get('id')

        try:
            transaction = Transaction.objects.get(payme_transaction_id=payme_transaction_id)
        except Transaction.DoesNotExist:
            return self.get_error_response('transaction_not_found', request_id)


        # ======== Check the transaction state ========
        if transaction.state == 1:
        # ==== Transaction is created, can perform ====
        #     print(f"Transaction State: {transaction.state}")
            transaction.status = True
            transaction.perform_time = timezone.now()
            transaction.state = 2 # == Update the state to 2 (completed) ==
            # print(f"Updated the state to 2 as completed: {transaction.state}")
            transaction.save()
            # print(f"Saved transaction: {transaction}")

            if transaction.order:
                transaction.order.is_paid = True
                transaction.order.save()
            return self.get_success_response(
                {
                    "perform_time": int(transaction.perform_time.timestamp() * 1000),
                    "transaction": payme_transaction_id,
                    "state": 2,
                },
                request_id
            )
        elif transaction.state == 2:
            # ==== Transaction already performed, return same result ====
            return self.get_success_response(
                {
                    "perform_time":int(transaction.perform_time.timestamp() * 1000),
                    "transaction":payme_transaction_id,
                    "state":2,
                },
                request_id
            )
        elif transaction.state in (-1, -2):
            # ==== transaction is cancelled, cannot perform ====
            return self.get_error_response('transaction_cannot_perform', request_id)
        else:
            # ==== unknown state ====
            return self.get_error_response('unable_to_perform', request_id)


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

            payme_transaction_id = params.get('id')
            reason = params.get('reason', 1)

            try:
                transaction = Transaction.objects.get(payme_transaction_id=payme_transaction_id)
            except Transaction.DoesNotExist:
                return self.get_error_response('transaction_not_found', request_id)

            if transaction.state == 1:
                # ==== Transaction is in created state, can cancel ====
                transaction.reason = reason
                transaction.state = -1 # As per Payme's specification for canceled before perform
                transaction.cancel_time = timezone.now()
                transaction.order.save()
            elif transaction.state == 2:
                transaction.reason = reason
                transaction.state = -2 # As per Payme's specification for canceled after perform
                transaction.cancel_time = timezone.now()
                transaction.save()
            else:
                # ==== Transaction is already cancelled, do nothing ====
                pass

            if transaction.order:
                transaction.order.is_paid = False
                transaction.order.save()

            return self.get_success_response(
                {
                    "cancel_time":int(transaction.cancel_time.timestamp() * 1000),
                    "transaction":payme_transaction_id,
                    "state":transaction.state
                },
                request_id
            )

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)


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

            payme_transaction_id = params.get('id')

            try:
                transaction = Transaction.objects.get(payme_transaction_id=payme_transaction_id)
            except Transaction.DoesNotExist:
                return self.get_error_response('transaction_not_found', request_id)

            response_data = {
                "create_time":int(transaction.date_time.timestamp() * 1000),
                "perform_time":int(transaction.perform_time.timestamp() * 1000) if transaction.perform_time else 0,
                "cancel_time":int(transaction.cancel_time.timestamp() * 1000) if transaction.cancel_time else 0,
                "transaction":payme_transaction_id,
                "state": transaction.state,
                "reason": transaction.reason
            }

            return self.get_success_response(response_data, request_id)

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)


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
                date_time__gte=from_date, date_time__lte=to_date, payment_system='Payme', )

            response_date = {"transactions":[
                {"id":str(t.id), "time":int(t.date_time.timestamp() * 1000), "amount":int(t.amount * 100),
                    "account":{"order_id":t.order._id if t.order else None, },
                    "create_time":int(t.date_time.timestamp() * 1000),
                    "perform_time":int(t.date_time.timestamp() * 1000) if t.status else 0, "cancel_time":0,
                    "transaction":str(t.id), "state":2 if t.status else 1, "reason":None} for t in transactions]}

            return self.get_success_response(response_date, request_id)

        except Exception as e:
            return self.get_error_response('unable_to_perform', request_id)