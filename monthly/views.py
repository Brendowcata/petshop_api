from rest_framework import viewsets
from monthly.models import MonthlyModel
from monthly.serializers import MonthlySerializer


class MonthlyViewSet(viewsets.ModelViewSet):
    """Displaying all schedules / Exibindo todos os agendamentos"""
    queryset = MonthlyModel.objects.all()
    serializer_class = MonthlySerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    ordering_fields = ['date_initial', 'date_final', 'value_money', 'customer', 'animal']
    search_fields = ['date_initial', 'date_final', 'customer',]
    filterset_fields = ['date_initial', 'date_final', 'value_money', 'customer', 'animal',]