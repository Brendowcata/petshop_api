from rest_framework import serializers
from monthly.models import MonthlyModel
from monthly.validators import *

class MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyModel
        fields = [
            "id",
            "date_initial",
            "date_final",
            "value_money",
            "amount_paid",
            "scheduling_amount",
            "animal"
        ]

class MonthlyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyModel
        fields = [
            "id",
            "date_initial",
            "date_final",
            "value_money",
            "amount_paid",
            "scheduling_amount",
            "animal"
        ]
    
    def validate(self, data):
        if not date_initial_smaller_date_final(data['date_initial'], data['date_final']):
            raise serializers.ValidationError(
                {'Date': "O Tempo inicial deve ser menor que o tempo final!"}
            )

        if not date_initial_greater_today(data['date_initial']):
            raise serializers.ValidationError(
                {'Date': "A data inicial deve ser maior ou igual que hoje!"}
            )
        
        if not value_money_isPositive(data['value_money']):
            raise serializers.ValidationError(
                {'Value_money': "O valor deve ser maior que 0"}
            )

        if not amount_paid_isPositive(data['amount_paid']):
            raise serializers.ValidationError(
                {'Amount_paid': "O valor deve ser maior que 0"}
            )

        return data