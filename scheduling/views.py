from rest_framework import viewsets

from scheduling.models import SchedulingModel
from scheduling.serializers import SchedulingPostSerializer, SchedulingSerializer

class SchedulingViewSet(viewsets.ModelViewSet):
    """Displaying all schedules / Exibindo todos os agendamentos"""
    queryset = SchedulingModel.objects.all()
    serializer_class = SchedulingSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    ordering_fields = ['date_appointment', 'value_money', 'animal']
    search_fields = ['date_appointment', 'animal',]
    filterset_fields = ['bath', 'clipping', 'hydration', 'clearance', 'dyeing', 
    'brush_teeth', 'cut_nails', 'transport', 'date_appointment', 
    'value_money', 'animal']

    def get_serializer_class(self):

        if self.request.method in ['POST']:
            return SchedulingPostSerializer
        return SchedulingSerializer