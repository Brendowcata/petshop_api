from rest_framework import viewsets

from pet.models import PetModel
from pet.serializers import PetPostSerializer, PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    """Displaying all pets / Exibindo todos os animais de estimação"""
    queryset = PetModel.objects.all()
    serializer_class = PetSerializer
    http_method_names = [
        'get', 
        'post', 
        'put', 
        'patch', 
        'delete',
        ]

    ordering_fields = [
        'customer', 
        'gender', 
        'size'
        ]

    search_fields = [
        'customer', 
        'name',
        'external_id',
        ]

    filterset_fields = [
        'name', 
        'gender', 
        'breed', 
        'size', 
        'color', 
        'birth_date', 
        'customer'
        ]

    def get_serializer_class(self):

        if self.request.method in ['POST']:
            return PetPostSerializer
        return PetSerializer
