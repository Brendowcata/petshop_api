from django.db import models
import uuid

class CustomerModel(models.Model):
    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        ) #id

    name = models.CharField(
        max_length=100, 
        db_column="NAME"
        ) #Nome
    

    cpf = models.CharField(
        max_length=14,
        db_column="CPF"
        )

    email = models.EmailField(
        db_column="EMAIL"
        ) #E-mail
    
    telephone = models.CharField(
        max_length=14,
        db_column="TELEPHONE"
        ) #Telefone

    phone_number = models.CharField(
        max_length=15, 
        blank=True,
        db_column="PHONE_NUMBER"
        ) #Celular

    class Meta:
        db_table = "CUSTOMER"
        verbose_name = "customer"
        verbose_name_plural = "customers"

    def __str__(self) -> str:
        return self.name