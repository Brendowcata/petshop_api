from rest_framework import serializers

from animal.models import AnimalModel


class AnimalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnimalModel
        fields = [
            "id",
            "name",
            "gender",
            "breed",
            "size",
            "color",
            "birth_date",
            "observation",
            "customer",
        ]