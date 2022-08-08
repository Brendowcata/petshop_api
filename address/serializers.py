from rest_framework import serializers
from address.models import AddressModel
from address.validators import *

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressModel
        fields = [
            "id",
            "external_id",
            "street",
            "neighborhood",
            "city",
            "state",
            "zip_code",
            "house_number",
            "customer"
        ]

class AddressPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = [
            "id",
            "external_id",
            "street",
            "neighborhood",
            "city",
            "state",
            "zip_code",
            "house_number",
            "customer"
        ]
    
    def validate(self, data):
        if not city_isValid(data['city']):
            raise serializers.ValidationError(
                {'City': "Este campo não deve conter números!"}
            )
        
        if not zip_code_isValid(data['zip_code']):
            raise serializers.ValidationError(
                {'Zip_code': "Este campo deve conter 9 dígitos! Favor utilizar este formato XXXXX-XXX"}
            )
        
        if not house_number_isValid(data['house_number']):
            raise serializers.ValidationError(
                {'House_number': "Este campo deve incluir apenas números!"}
            )

        return data
    