import uuid
from django.db import models

from customer.models import CustomerModel
from animal.models import AnimalModel
from payment.models import PaymentModel

class MonthlyModel(models.Model):

    external_id = models.UUIDField(
        db_column="EXTERNAL_ID", 
        editable=False, 
        unique=True,
        default= uuid.uuid4
        ) #id externo

    date_initial = models.DateField(
        db_column="DATE_INITIAL"
        ) # Data inicial
    
    date_final = models.DateField(
        db_column="DATE_FINAL"
        ) #Data final

    scheduling_amount = models.PositiveIntegerField(
        db_column="SCHEDULING_AMOUNT"
    ) #Quantidade de agendamento   

    payment = models.ForeignKey(
        PaymentModel,
        on_delete=models.CASCADE,
        null=False,
        db_column="PAYMENT"
    ) #Pagamento
    
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
    

