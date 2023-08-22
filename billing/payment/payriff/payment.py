from dataclasses import dataclass

@dataclass
class Order:
    amount: float
    currency: str
    status_code: str
    order_id: str
    session_id: str
    payment_url: str
    transaction_id: str

@dataclass
class OrderStatus:
    code: str
    message: str
    orderId: str
    orderStatus: str

@dataclass
class Refund:
    code: str
    internalMessage: str
    message: str