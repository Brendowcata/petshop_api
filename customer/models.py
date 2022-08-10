from django.db import models
import uuid

class CustomerModel(models.Model):
    external_id = models.UUIDField(
        editable=False, 
        unique=True,
        default= uuid.uuid4
        ) #id externo
    

    name = models.CharField(
        max_length=150, 
        ) #Nome
    

    cpf = models.CharField(
        unique=True,
        max_length=14,
        ) #CPF
    
    birth_date = models.DateField(
        blank =True,
        null=True
    ) #Data de aniversario

    email = models.EmailField(
        null=True,
        blank=True,
        ) #E-mail
    
    telephone = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        ) #Telefone

    phone_number = models.CharField(
        max_length=15,
        ) #Celular

    class Meta:
        db_table = "CUSTOMER"
        verbose_name = "customer"
        verbose_name_plural = "customers"

    def __str__(self) -> str:
        return self.name