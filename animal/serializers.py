from rest_framework import serializers

from animal.models import AnimalModel
from animal.validators import *


class AnimalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnimalModel
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

class AnimalPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
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
        if not name_isValid(data['name']):
            raise serializers.ValidationError(
                {'Name': "Este campo não deve conter números!"}
            )

        return data