import uuid
from django.db import models

from payment.enums import Payment_Type

class PaymentModel(models.Model):

    external_id = models.UUIDField(
        editable=False, 
        unique=True,
        default= uuid.uuid4
    ) #id externo

    value_money = models.FloatField(
    ) #Valor em dinheiro

    amount_paid = models.FloatField(
    ) #Valor Pago

    payment_type = models.CharField(
        max_length=14,
        choices=Payment_Type.choices(),
    ) #Tipo de pagamento

    registration_date = models.DateTimeField(
    ) #Data de registro

    pay_day = models.DateField(
    ) #Data de pagamento
    
    is_paid = models.BooleanField(
        default=False,
    ) #Está Pago

    class Meta:
        db_table = "PAYMENT"
        verbose_name = "payment"
        verbose_name_plural = "payments"

    def __str__(self) -> str:
        return f'{self.payment_type} - {self.registration_date.strftime("%m/%d/%Y")} - Value: {self.value_money}'