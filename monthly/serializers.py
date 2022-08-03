from rest_framework import serializers
from monthly.models import MonthlyModel

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
            "customer",
            "animal"
        ]