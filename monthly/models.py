import uuid
from django.db import models

from customer.models import CustomerModel
from pet.models import PetModel
from payment.models import PaymentModel

class MonthlyModel(models.Model):

    external_id = models.UUIDField(
        editable=False, 
        unique=True,
        default= uuid.uuid4
        ) #id externo

    date_initial = models.DateField(
        ) # Data inicial
    
    date_final = models.DateField(
        ) #Data final

    scheduling_amount = models.PositiveIntegerField(
    ) #Quantidade de agendamento   

    payment = models.ForeignKey(
        PaymentModel,
        on_delete=models.CASCADE,
        null=False,
    ) #Pagamento
    
    pet = models.ForeignKey(
        PetModel,
        on_delete=models.CASCADE,
        null=False,
    ) #Animal
    
    class Meta:
        db_table = "MONTHLY"
        verbose_name = "monthly"
        verbose_name_plural = "monthlies"
    
    def __str__(self) -> str:
         return f'{self.customer} - {self.date_initial.strftime("%m/%d/%Y")} - {self.date_final.strftime("%m/%d/%Y")}'
    

