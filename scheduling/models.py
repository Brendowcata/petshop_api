from django.db import models
from animal.models import AnimalModel
import uuid
from payment.models import PaymentModel

from scheduling.enums import Clipping_Type

class SchedulingModel(models.Model):

    external_id = models.UUIDField(
        db_column="EXTERNAL_ID", 
        editable=False, 
        unique=True,
        default= uuid.uuid4
    ) #id externo

    bath = models.BooleanField(
        default=False,
        db_column="BATH"
    ) #Banho

    clipping = models.CharField(
        max_length=15,
        choices=Clipping_Type.choices(),
        db_column="TYPE_CLIPPING"
    ) #Tipo de Tosa

    hydration = models.BooleanField(
        default=False,
        db_column="HYDRATION"
    ) #Hidratação

    clearance = models.BooleanField(
        default=False,
        db_column="CLEARANCE"
    ) #Desembaraçamento

    brush_teeth = models.BooleanField(
        default=False,
        db_column="BRUSH_TEETH"
    ) #Escovar os dentes

    cut_nails = models.BooleanField(
        default=False,
        db_column="CUT_NAILS"
    ) #Cortar as unhas

    transport = models.BooleanField(
        default=False,
        db_column="TRANSPORT"
    ) #Transporte

    date_appointment = models.DateField(
        db_column="DATE_SCHEDULING"
    ) #Data de Agendamento

    hour_appointment = models.TimeField(
        db_column="HOUR_APPOINTMENT"
    ) #Hora do Agendamento

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
    ) # Animal

    class Meta:
        db_table = "SCHEDULING"
        verbose_name = "scheduling"
        verbose_name_plural = "schedules"

    def __str__(self) -> str:
        return f'{self.animal} - {self.date_appointment.strftime("%m/%d/%Y")}'