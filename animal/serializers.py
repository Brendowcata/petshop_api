from rest_framework import serializers

from animal.models import AnimalModel


class AnimalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnimalModel
        fields = [
            "id",
            "name",
            "breed",
            "size",
            "color",
            "observation",
            "customer",
        ]