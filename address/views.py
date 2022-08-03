from rest_framework import viewsets
from address.models import AddressModel
from address.serializers import AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
    """Displaying all addresses / Exibindo todos os endereços"""
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    ordering_fields = ['customer']
    search_fields = ['customer']
    filterset_fields = ['street', 'neighborhood', 'city', 'state', 'zip_code', 'customer']
