from django.db import models
import uuid

class CustomerModel(models.Model):
    external_id = models.UUIDField(
        db_column="EXTERNAL_ID", 
        editable=False, 
        unique=True,
        default= uuid.uuid4
        ) #id externo
    

    name = models.CharField(
        max_length=150, 
        db_column="NAME"
        ) #Nome
    

    cpf = models.CharField(
        unique=True,
        max_length=14,
        db_column="CPF"
        ) #CPF
    
    birth_date = models.DateField(
        db_column="BIRTH_DATE",
        blank =True,
        null=True
    ) #Data de aniversario

    email = models.EmailField(
        null=True,
        blank=True,
        db_column="EMAIL"
        ) #E-mail
    
    telephone = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        db_column="TELEPHONE"
        ) #Telefone

    phone_number = models.CharField(
        max_length=15,
        db_column="PHONE_NUMBER"
        ) #Celular

    class Meta:
        db_table = "CUSTOMER"
        verbose_name = "customer"
        verbose_name_plural = "customers"

    def __str__(self) -> str:
        return self.name