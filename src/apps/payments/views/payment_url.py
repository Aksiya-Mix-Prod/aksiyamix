import base64
from decimal import Decimal
from dataclasses import dataclass

from django.conf import settings

# PAYME_ID = settings.PAYME_ID
# PAYME_ACCOUNT = settings.PAYME_ACCOUNT
# PAYME_CALL_BACK_URL = settings.PAYME_CALL_BACK_URL # this is our endpoint which we give to Payme to setup our
# business account
# PAYME_URL = settings.PAYME_URL
PAYME_URL='https://checkout.paycom.uz' # always the same!


@dataclass
class GeneratePayLink:

    order_id: str
    amount: Decimal

    def generate_link(self) -> str:

        generated_pay_link: str = "{payme_url}/{encode_params}"
        params: str = 'm={payme_id};ac.{payme_account}={order_id};a={amount};c={call_back_url}'

        params = params.format(
            payme_id=settings.PAYME_USERNAME, # test id or pro id
            payme_account='fintech_test', # u get this after opening a payme busienss account
            order_id=self.order_id,
            amount=self.amount,
            call_back_url='https://9293-94-158-60-167.ngrok-free.app/api/v1/payments/payme/merchant/'
        )
        encode_params = base64.b64encode(params.encode("utf-8"))
        return generated_pay_link.format(
            payme_url=PAYME_URL,
            encode_params=str(encode_params, 'utf-8')
        )