from rest_framework import viewsets

from scheduling.models import SchedulingModel
from scheduling.serializers import SchedulingSerializer

class SchedulingViewSet(viewsets.ModelViewSet):
    """Displaying all schedules / Exibindo todos os agendamentos"""
    queryset = SchedulingModel.objects.all()
    serializer_class = SchedulingSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']