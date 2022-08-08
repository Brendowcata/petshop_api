from payment.models import PaymentModel
from datetime import datetime
from payment.validators import *
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentModel
        fields = [
            "id",
            "external_id",
            "value_money",
            "amount_paid",
            "is_paid",
            "payment_type",
            "registration_date",
            "pay_day",
        ]

class PaymentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentModel
        fields = [
            "id",
            "external_id",
            "value_money",
            "amount_paid",
            "is_paid",
            "payment_type",
            "pay_day",
        ]
    
    def create(self, validated_data):
        validated_data['registration_date'] = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
        return super().create(validated_data)
    
    def validate(self, data):

        if not pay_day_greater_or_equal_today(data['pay_day']):
            raise serializers.ValidationError(
                {'Pay_day': "A data inicial deve ser maior ou igual que hoje!"}
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