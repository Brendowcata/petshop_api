
from payment.models import PaymentModel
from payment.serializers import PaymentPostSerializer, PaymentSerializer
from rest_framework import viewsets

class PaymentViewSet(viewsets.ModelViewSet):
    """Displaying all payments / Exibindo todos os pagamentos"""
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    ordering_fields = ['payment_type', 'registration_date', 'pay_day']
    search_fields = ['external_id',]
    filterset_fields = ['value_money', 'amount_paid', 'payment_type',
    'registration_date', 'pay_day',]

    def get_serializer_class(self):

        if self.request.method in ['POST']:
            return PaymentPostSerializer
        return PaymentSerializer