from django.db import models
from animal.enums import Breed_Type, Color_Type, Gender_Type, Size_Type
from customer.models import CustomerModel
import uuid


class AnimalModel(models.Model):

    external_id = models.UUIDField(
        db_column="EXTERNAL_ID", 
        editable=False, 
        unique=True,
        default= uuid.uuid4
        ) #id externo

    name = models.CharField(
        max_length=100, 
        db_column="NAME"
        ) #Nome
    
    gender = models.CharField(
        max_length=1,
        choices=Gender_Type.choices(),
        blank=False,
        null=False,
        db_column="GENDER"
    ) #Gênero

    breed = models.CharField(
        max_length=30,
        choices=Breed_Type.choices(), 
        blank=False, 
        null=False, 
        db_column="BREED",
        ) #Raça

    size = models.CharField(
        max_length=7,
        choices=Size_Type.choices(), 
        blank=False, 
        null=False, 
        db_column="SIZE"
        ) #Tamanho

    color = models.CharField(
        max_length=15,
        choices=Color_Type.choices(), 
        blank=False, 
        null=False, 
        db_column="COLOR"
        ) #Cor

    birth_date = models.DateField(
        db_column="BIRTH_DATE",
        blank =True,
        null=True
    ) #Data de aniversario

    observation = models.TextField(
        blank=True,
        db_column="OBSERVATION"
        ) #Observação

    customer = models.ForeignKey(
        CustomerModel, 
        on_delete=models.CASCADE, 
        related_name="animal",
        null=False
        ) #Cliente
    
    class Meta:
        db_table = "ANIMAL"
        verbose_name = "animal"
        verbose_name_plural = "animals"


    def __str__(self) -> str:
        return f"{self.name} - dono: {self.customer}"