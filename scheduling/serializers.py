from dataclasses import field
from rest_framework import serializers
from scheduling.models import SchedulingModel

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