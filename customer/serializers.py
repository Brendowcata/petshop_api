from rest_framework import serializers
from customer.models import CustomerModel
from animal.serializers import AnimalSerializer
from customer.validators import *

class CustomerSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(many = True, read_only=True)

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
            'animal'
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
            'animal'
            ]
    
    def validate(self, data):
        if not telephone_isValid(data['telephone']):
            raise serializers.ValidationError(
                {'Telephone': "Este campo deve ter 14 dígitos! Favor utilizar este formato (XX) XXXX-XXXX"}
                )
        
        if not name_isValid(data['name']):
            raise serializers.ValidationError(
                {'Name': "Este campo não deve conter números!"}
            )
        
        if not phone_number_isValid(data['phone_number']):
            raise serializers.ValidationError(
                {'Phone_number': "Este campo deve ter 15 dígitos! Favor utilizar este formato (XX) 9XXXX-XXXX"}
                )
        
        if not cpf_isValid(data['cpf']):
            raise serializers.ValidationError(
                {'CPF': "Digite um CPF Válido!"}
            )

        return data