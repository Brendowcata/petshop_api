import uuid
from django.db import models
from address.enums import States_Type

from customer.models import CustomerModel

class AddressModel(models.Model):

    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        )

    street = models.CharField(
        max_length=100, 
        db_column="STREET"
        ) #Rua

    neighborhood = models.CharField(
        max_length=100, 
        db_column="NEIGHBORHOOD"
        ) #Bairro

    city = models.CharField(
        max_length=50, 
        db_column="CITY"
        ) #Cidade

    state = models.CharField(
        max_length=2, 
        choices=States_Type.choices(), 
        blank=False, 
        null=False, 
        db_column="STATE"
        ) #Estado/UF

    zip_code = models.CharField(
        max_length=9, 
        db_column="ZIP_CODE"
        ) #CEP

    house_number = models.CharField(
        max_length=5, 
        db_column="HOUSE_NUMBER"
        ) #Número do local
    
    customer = models.ForeignKey(
        CustomerModel, 
        on_delete=models.CASCADE,
        null=False,
        db_column="CUSTOMER") #Cliente
    
    class Meta:
        db_table = "ADDRESS"
        verbose_name = "address"
        verbose_name_plural = "addresses"
    
    def __str__(self) -> str:
        return f"{self.street}, {self.house_number}"
