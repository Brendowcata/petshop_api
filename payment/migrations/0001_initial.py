# Generated by Django 4.0.6 on 2022-08-10 16:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('value_money', models.FloatField()),
                ('amount_paid', models.FloatField()),
                ('payment_type', models.CharField(choices=[('CARTAO_CREDITO', 'Cartão de Crédito'), ('CARTAO_DEBITO', 'Cartão de Débito'), ('PIX', 'Pix'), ('DINHEIRO', 'Dinheiro'), ('TRANSFERENCIA', 'Transferência bancária')], max_length=14)),
                ('registration_date', models.DateTimeField()),
                ('pay_day', models.DateField()),
                ('is_paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
                'db_table': 'PAYMENT',
            },
        ),
    ]