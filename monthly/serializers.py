from rest_framework import serializers
from monthly.models import MonthlyModel
from monthly.validators import date_initial_greater_today, date_initial_smaller_date_final

class MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyModel
        fields = [
            "id",
            "external_id",
            "date_initial",
            "date_final",
            "scheduling_amount",
            "payment",
            "pet",
        ]

class MonthlyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyModel
        fields = [
            "id",
            "external_id",
            "date_initial",
            "date_final",
            "scheduling_amount",
            "payment",
            "pet",
        ]
    
    def validate(self, data):
        if not date_initial_smaller_date_final(data['date_initial'], data['date_final']):
            raise serializers.ValidationError(
                {'date': "O Tempo inicial deve ser menor que o tempo final!"}
            )

        if not date_initial_greater_today(data['date_initial']):
            raise serializers.ValidationError(
                {'date': "A data inicial deve ser maior ou igual que hoje!"}
            )
        
        return data