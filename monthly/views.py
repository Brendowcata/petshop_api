from rest_framework import viewsets
from monthly.models import MonthlyModel
from monthly.serializers import MonthlyPostSerializer, MonthlySerializer


class MonthlyViewSet(viewsets.ModelViewSet):
    """Displaying all schedules / Exibindo todos os agendamentos"""
    queryset = MonthlyModel.objects.all()
    serializer_class = MonthlySerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    ordering_fields = ['date_initial', 'date_final', 'payment', 'animal']
    search_fields = ['date_initial', 'date_final',]
    filterset_fields = ['date_initial', 'date_final', 'payment', 'animal',]

    def get_serializer_class(self):

        if self.request.method in ['POST']:
            return MonthlyPostSerializer
        return MonthlySerializer