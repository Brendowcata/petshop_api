from pyexpat import model
from rest_framework import serializers
from address.models import AddressModel

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressModel
        fields = [
            "street",
            "neighborhood",
            "city",
            "state",
            "zip_code",
            "house_number",
            "customer"
        ]