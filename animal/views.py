from rest_framework import viewsets

from animal.models import AnimalModel
from animal.serializers import AnimalPostSerializer, AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    """Displaying all animals / Exibindo todos os animais"""
    queryset = AnimalModel.objects.all()
    serializer_class = AnimalSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    ordering_fields = ['customer', 'gender', 'size']
    search_fields = ['customer', 'name']
    filterset_fields = ['name', 'gender', 'breed', 'size', 'color', 'birth_date', 'customer']

    def get_serializer_class(self):

        if self.request.method in ['POST']:
            return AnimalPostSerializer
        return AnimalSerializer
