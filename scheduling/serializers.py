from dataclasses import field
from rest_framework import serializers
from scheduling.models import SchedulingModel
from scheduling.validators import *

class SchedulingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchedulingModel
        fields = [
            "id",
            "bath",
            "clipping",
            "hydration",
            "clearance",
            "dyeing",
            "brush_teeth",
            "cut_nails",
            "transport",
            "date_appointment",
            "hour_appointment",
            "value_money",
            "amount_paid",
            "animal",
        ]

class SchedulingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedulingModel
        fields = [
            "id",
            "bath",
            "clipping",
            "hydration",
            "clearance",
            "dyeing",
            "brush_teeth",
            "cut_nails",
            "transport",
            "date_appointment",
            "hour_appointment",
            "value_money",
            "amount_paid",
            "animal",
        ]
    
    def validate(self, data):

        if not date_appointment_greater_today(data['date_appointment']):
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