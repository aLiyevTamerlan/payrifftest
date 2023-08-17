from django.urls import path
from billing.views import PaymentCreateAPIView
urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
]
