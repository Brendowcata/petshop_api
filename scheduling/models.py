from django.db import models
from pet.models import PetModel
import uuid
from payment.models import PaymentModel

from scheduling.enums import Clipping_Type

class SchedulingModel(models.Model):

    external_id = models.UUIDField(
        editable=False, 
        unique=True,
        default= uuid.uuid4
    ) #id externo

    bath = models.BooleanField(
        default=False,
    ) #Banho

    clipping = models.CharField(
        max_length=15,
        choices=Clipping_Type.choices(),
    ) #Tipo de Tosa

    hydration = models.BooleanField(
        default=False,
    ) #Hidratação

    clearance = models.BooleanField(
        default=False,
    ) #Desembaraçamento

    brush_teeth = models.BooleanField(
        default=False,
    ) #Escovar os dentes

    cut_nails = models.BooleanField(
        default=False,
    ) #Cortar as unhas

    transport = models.BooleanField(
        default=False,
    ) #Transporte

    date_appointment = models.DateField(
    ) #Data de Agendamento

    hour_appointment = models.TimeField(
    ) #Hora do Agendamento

    payment = models.ForeignKey(
        PaymentModel,
        on_delete=models.CASCADE,
        null=False,
    ) #Pagamento

    pet = models.ForeignKey(
        PetModel,
        on_delete=models.CASCADE,
        null=False,
    ) # Animal

    class Meta:
        db_table = "SCHEDULING"
        verbose_name = "scheduling"
        verbose_name_plural = "schedules"

    def __str__(self) -> str:
        return f'{self.animal} - {self.date_appointment.strftime("%m/%d/%Y")}'