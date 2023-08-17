from django.conf import settings
from .payment import Order
import requests, json

class PayriffGateway:
    BASE_URL = 'https://api.payriff.com/api/v2/'
    SECRET_KEY = settings.PAYRIFF_SECRET_KEY
    def __init__(
        self,
        merchant_id: str,
        approve_url: str,
        cancel_url: str,
        decline_url: str) -> None:
        self.merchant_id = merchant_id
        self.approve_url = approve_url
        self.cancel_url = cancel_url
        self.decline_url = decline_url
        self.__order_instance = None


    def __post(self, method_name: str, payload: dict) -> dict:
        url = f"{self.BASE_URL}{method_name}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.SECRET_KEY,
            "Accept": "*",
            "Connection": "keep-alive",
        }
        req = requests.post(
            url, 
            data=payload,
            headers=headers,
        )
        return req.json()

    def __build_json_payload(self, data: dict) -> dict:
        return json.dumps(data)
    
    def __build_order_object(self, order_data: dict , result: dict):
        self.__order_instance = Order(
            amount=order_data["body"]["amount"],
            currency=order_data["body"]["currencyType"],
            status_code=result["code"],
            order_id=result["payload"]["orderId"],
            session_id=result["payload"]["sessionId"],
            payment_url=result["payload"]["paymentUrl"],
            transaction_id=result["payload"]["transactionId"]
        )

    def get_order(self):
        return self.__order_instance
    
    def create_order(
        self,
        amount: float,
        currency: str,
        direct_pay: bool = True,
        description: str = None,
        language: str = "AZ") -> dict:
        order_data = {
            "body": {
                "amount": amount,
                "approveURL": self.approve_url,
                "cancelURL": self.cancel_url,
                "currencyType": currency,
                "declineURL": self.decline_url,
                "description": description,
                "directPay": direct_pay,
                "language": language,
            },
            "merchant": self.merchant_id,
        }
        json_payload = self.__build_json_payload(data=order_data)
        result = self.__post(
            method_name="createOrder",
            payload=json_payload,
        )

        self.__build_order_object(order_data=order_data, result=result)
        order = self.get_order()

        return {
            "status_code": order.status_code,
            "payment_url": order.payment_url, 
            "session_id": order.session_id, 
            "order_id": order.order_id
        }