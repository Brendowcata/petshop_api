from django.db import models
from pet.enums import BreedType, ColorType, GenderType, SizeType
from customer.models import CustomerModel
import uuid


class PetModel(models.Model):

    external_id = models.UUIDField(
        editable=False, 
        unique=True,
        default= uuid.uuid4
        ) #id externo

    name = models.CharField(
        max_length=100, 
        ) #Nome
    
    gender = models.CharField(
        max_length=1,
        choices=GenderType.choices(),
        blank=False,
        null=False,
    ) #Gênero

    breed = models.CharField(
        max_length=30,
        choices=BreedType.choices(), 
        blank=False, 
        null=False, 
        ) #Raça

    size = models.CharField(
        max_length=7,
        choices=SizeType.choices(), 
        blank=False, 
        null=False, 
        ) #Tamanho

    color = models.CharField(
        max_length=15,
        choices=ColorType.choices(), 
        blank=False, 
        null=False, 
        ) #Cor

    birth_date = models.DateField(
        blank =True,
        null=True
    ) #Data de aniversario

    observation = models.TextField(
        blank=True,
        ) #Observação

    customer = models.ForeignKey(
        CustomerModel, 
        on_delete=models.CASCADE, 
        related_name="pet",
        null=False
        ) #Cliente
    
    class Meta:
        db_table = "PET"
        verbose_name = "pet"
        verbose_name_plural = "pets"


    def __str__(self) -> str:
        return f"{self.name} - dono: {self.customer}"