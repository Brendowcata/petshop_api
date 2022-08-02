import uuid
from django.db import models

from apps.customer.models import CustomerModel

class AddressModel(models.Model):

    STATES = (
        ('SC', 'Santa Catarina'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapa'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceara'),
        ('ES', 'Espirito Santo'),
        ('GO', 'Goias'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Para'),
        ('PB', 'Paraiba'),
        ('PR', 'Parana'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piaui'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande Do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
        ('DF', 'Distrito Federal')
    )

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
        choices=STATES, 
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
        on_delete=models.DO_NOTHING,
        null=False,
        db_column="CUSTOMER") #Cliente
    
    class Meta:
        db_table = "ADDRESS"
        verbose_name = "address"
        verbose_name_plural = "addresses"
