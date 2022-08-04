import uuid
from django.db import models

from customer.models import CustomerModel
from animal.models import AnimalModel

class MonthlyModel(models.Model):

    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        ) #id

    date_initial = models.DateField(
        db_column="DATE_INITIAL"
        ) # Data inicial
    
    date_final = models.DateField(
        db_column="DATE_FINAL"
        ) #Data final

    value_money = models.FloatField(
        db_column="VALUE_MONEY"
        ) #Valor em dinheiro

    amount_paid = models.FloatField(
        db_column="AMOUNT_PAID"
        ) #Valor Pago

    scheduling_amount = models.PositiveIntegerField(
        db_column="SCHEDULING_AMOUNT"
    ) #Quantidade de agendamento   
    
    animal = models.ForeignKey(
        AnimalModel,
        on_delete=models.CASCADE,
        null=False,
        db_column="ANIMAL"
    ) #Animal
    
    class Meta:
        db_table = "MONTHLY"
        verbose_name = "monthly"
        verbose_name_plural = "monthlies"
    
    def __str__(self) -> str:
         return f'{self.customer} - {self.date_initial.strftime("%m/%d/%Y")} - {self.date_final.strftime("%m/%d/%Y")}'
    

