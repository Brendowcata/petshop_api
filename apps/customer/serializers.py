from rest_framework import serializers
from customer.models import CustomerModel

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerModel
        fields = [
            "id",
            "name",
            "cpf",
            "email",
            "telephone",
            "phone_number",
            ]