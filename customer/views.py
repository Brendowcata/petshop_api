from rest_framework import viewsets
from customer.models import CustomerModel
from customer.serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """Displaying all customers / Exibindo todos os clientes"""
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    ordering_fields = ['name', 'birth_date',]
    search_fields = ['name', 'cpf', 'telephone', 'phone_number',]
    filterset_fields = ['name', 'email', 'cpf', 'birth_date', 'telephone', 'phone_number',]