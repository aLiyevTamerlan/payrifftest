from django.conf import settings

from billing.payment.payriff import PayriffGateway

payriff_gateway = PayriffGateway(
    merchant_id = settings.PAYRIFF_MERCHANT_ID,
    approve_url = settings.PAYRIFF_APPROVE_URL,
    cancel_url = settings.PAYRIFF_CANCEL_URL,
    decline_url = settings.PAYRIFF_DECLINE_URL,
)