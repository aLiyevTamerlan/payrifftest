from rest_framework.views import APIView
from rest_framework.response import Response
from billing.payment.payment import payriff_gateway

class PaymentCreateAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        currency = request.data.get('currency')
        description = request.data.get('description')
        
        r = payriff_gateway.create_order(
            amount=amount,
            currency=currency,
            description=description,
        )

        return Response({
            'data': r,
        })

