from django.db import models
from animal.models import AnimalModel
import uuid

from scheduling.enums import Clipping_Type

class SchedulingModel(models.Model):

    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        ) #id

    bath = models.BooleanField(
        default=False,
        db_column="BATH"
        ) #Banho

    clipping = models.CharField(
        max_length=15,
        choices=Clipping_Type.choices(),
        blank=True,
        null=True,
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

    value_money = models.FloatField(
        db_column="VALUE_MONEY"
    ) #Valor em dinheiro

    amount_paid = models.FloatField(
        db_column="AMOUNT_PAID"
        ) #Valor Pago

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