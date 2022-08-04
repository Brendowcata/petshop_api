from rest_framework import serializers
from customer.models import CustomerModel
from animal.serializers import AnimalSerializer

class CustomerSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(many = True, read_only=True)

    class Meta:
        model = CustomerModel
        fields = [
            "id",
            "name",
            "cpf",
            "birth_date",
            "email",
            "telephone",
            "phone_number",
            'animal'
            ]