import uuid
from django.db import models

from payment.enums import Payment_Type

class PaymentModel(models.Model):

    external_id = models.UUIDField(
        db_column="EXTERNAL_ID", 
        editable=False, 
        unique=True,
        default= uuid.uuid4
    ) #id externo

    value_money = models.FloatField(
        db_column="VALUE_MONEY"
    ) #Valor em dinheiro

    amount_paid = models.FloatField(
        db_column="AMOUNT_PAID"
    ) #Valor Pago

    payment_type = models.CharField(
        max_length=14,
        choices=Payment_Type.choices(),
        db_column="TYPE_CLIPPING"
    ) #Tipo de pagamento

    registration_date = models.DateTimeField(
        db_column="REGISTRATION_DATE"
    ) #Data de registro

    pay_day = models.DateField(
        db_column="PAY_DAY"
    ) #Data de pagamento
    
    is_paid = models.BooleanField(
        default=False,
        db_column="IS_PAID"
    ) #Está Pago

    class Meta:
        db_table = "PAYMENT"
        verbose_name = "payment"
        verbose_name_plural = "payments"

    def __str__(self) -> str:
        return f'{self.payment_type} - {self.registration_date.strftime("%m/%d/%Y")} - Value: {self.value_money}'