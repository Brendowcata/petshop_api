from rest_framework import viewsets
from customer.models import CustomerModel
from customer.serializers import CustomerPostSerializer, CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """Displaying all customers / Exibindo todos os clientes"""
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer

    http_method_names = [
        'get', 
        'post', 
        'put', 
        'patch',
        'delete',
        ]

    ordering_fields = [
        'name', 
        'birth_date',
        ]

    search_fields = [
        'name', 
        'cpf', 
        'telephone', 
        'phone_number',
        'external_id',
        ]

    filterset_fields = [
        'name', 
        'email', 
        'cpf', 
        'birth_date', 
        'telephone', 
        'phone_number',
        ]

    def get_serializer_class(self):

        if self.request.method in ['POST']:
            return CustomerPostSerializer
        return CustomerSerializer

        