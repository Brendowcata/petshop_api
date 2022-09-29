from rest_framework import serializers

from pet.models import PetModel
from pet.validators import is_name_valid


class PetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PetModel
        fields = [
            "id",
            "external_id",
            "name",
            "gender",
            "breed",
            "size",
            "color",
            "birth_date",
            "observation",
            "customer",
        ]

class PetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetModel
        fields = [
            "id",
            "external_id",
            "name",
            "gender",
            "breed",
            "size",
            "color",
            "birth_date",
            "observation",
            "customer",
        ]
        
    def validate(self, data):
        if not is_name_valid(data['name']):
            raise serializers.ValidationError(
                {'Name': "Este campo não deve conter números!"}
            )

        return data