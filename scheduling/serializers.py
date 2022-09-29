from dataclasses import field
from rest_framework import serializers
from scheduling.models import SchedulingModel
from scheduling.validators import date_appointment_greater_today

class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedulingModel
        fields = [
            "id",
            "external_id",
            "bath",
            "clipping",
            "hydration",
            "clearance",
            "brush_teeth",
            "cut_nails",
            "transport",
            "date_appointment",
            "hour_appointment",
            "payment",
            "pet",
        ]

class SchedulingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedulingModel
        fields = [
            "id",
            "external_id",
            "bath",
            "clipping",
            "hydration",
            "clearance",
            "brush_teeth",
            "cut_nails",
            "transport",
            "date_appointment",
            "hour_appointment",
            "payment",
            "pet",
        ]
    
    def validate(self, data):

        if not date_appointment_greater_today(data['date_appointment']):
            raise serializers.ValidationError(
                {'date': "A data inicial deve ser maior ou igual que hoje!"}
            )

        return data