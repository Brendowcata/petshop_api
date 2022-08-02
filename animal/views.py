from rest_framework import viewsets

from animal.models import AnimalModel
from animal.serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    """Displaying all animals / Exibindo todos os animais"""
    queryset = AnimalModel.objects.all()
    serializer_class = AnimalSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

