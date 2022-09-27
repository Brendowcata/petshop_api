from payment.models import PaymentModel
from datetime import datetime
from payment.validators import is_amount_paid_positive, is_value_money_positive, pay_day_greater_or_equal_today
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
                {'pay_day': "A data inicial deve ser maior ou igual que hoje!"}
            )
        
        if not is_value_money_positive(data['value_money']):
            raise serializers.ValidationError(
                {'value_money': "O valor deve ser maior que 0"}
            )

        if not is_amount_paid_positive(data['amount_paid']):
            raise serializers.ValidationError(
                {'amount_paid': "O valor deve ser maior que 0"}
            )

        return data