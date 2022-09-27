import uuid
from django.db import models

from customer.models import CustomerModel

class AddressModel(models.Model):

    external_id = models.UUIDField(
        editable=False, 
        unique=True,
        default= uuid.uuid4
        ) #id externo

    street = models.CharField(
        max_length=100, 
        ) #Rua

    neighborhood = models.CharField(
        max_length=100, 
        ) #Bairro

    city = models.CharField(
        max_length=50, 
        ) #Cidade

    zip_code = models.CharField(
        max_length=9, 
        ) #CEP

    house_number = models.CharField(
        max_length=5, 
        ) #Número do local
    
    customer = models.ForeignKey(
        CustomerModel, 
        on_delete=models.CASCADE,
        null=False,
        ) #Cliente
    
    class Meta:
        db_table = "ADDRESS"
        verbose_name = "address"
        verbose_name_plural = "addresses"
    
    def __str__(self) -> str:
        return f"{self.street}, {self.house_number}"
