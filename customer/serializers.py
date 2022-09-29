from rest_framework import serializers
from customer.models import CustomerModel
from pet.serializers import PetSerializer
from customer.validators import is_cpf_valid, is_name_valid, is_telephone_valid, is_phone_number_valid

class CustomerSerializer(serializers.ModelSerializer):
    pet = PetSerializer(many = True, read_only=True)

    class Meta:
        model = CustomerModel
        fields = [
            "id",
            "external_id",
            "name",
            "cpf",
            "birth_date",
            "email",
            "telephone",
            "phone_number",
            'pet',
            ]

class CustomerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = [
            "id",
            "external_id",
            "name",
            "cpf",
            "birth_date",
            "email",
            "telephone",
            "phone_number",
            'pet',
            ]
    
    def validate(self, data):
        if not is_telephone_valid(data['telephone']):
            raise serializers.ValidationError(
                {'telephone': "Este campo deve ter 14 dígitos! Favor utilizar este formato (XX) XXXX-XXXX"}
                )
        
        if not is_name_valid(data['name']):
            raise serializers.ValidationError(
                {'name': "Este campo não deve conter números!"}
            )
        
        if not is_phone_number_valid(data['phone_number']):
            raise serializers.ValidationError(
                {'phone_number': "Este campo deve ter 15 dígitos! Favor utilizar este formato (XX) 9XXXX-XXXX"}
                )
        
        if not is_cpf_valid(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': "Digite um CPF Válido!"}
            )

        return data