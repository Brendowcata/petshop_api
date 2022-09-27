from rest_framework import serializers
from address.models import AddressModel
from address.validators import is_city_valid, is_house_number_valid, is_zip_code_valid

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressModel
        fields = [
            "id",
            "external_id",
            "street",
            "neighborhood",
            "city",
            "zip_code",
            "house_number",
            "customer",
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
            "zip_code",
            "house_number",
            "customer",
        ]
    
    def validate(self, data):
        if not is_city_valid(data['city']):
            raise serializers.ValidationError(
                {'city': "Este campo não deve conter números!"}
            )
        
        if not is_zip_code_valid(data['zip_code']):
            raise serializers.ValidationError(
                {'zip_code': "Este campo deve conter 9 dígitos! Favor utilizar este formato XXXXX-XXX"}
            )
        
        if not is_house_number_valid(data['house_number']):
            raise serializers.ValidationError(
                {'house_number': "Este campo deve incluir apenas números!"}
            )

        return data
    