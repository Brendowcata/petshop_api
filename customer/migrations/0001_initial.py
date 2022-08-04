# Generated by Django 4.0.6 on 2022-08-04 14:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='NAME', max_length=100)),
                ('cpf', models.CharField(db_column='CPF', max_length=14, unique=True)),
                ('birth_date', models.DateField(blank=True, db_column='BIRTH_DATE', null=True)),
                ('email', models.EmailField(db_column='EMAIL', max_length=254)),
                ('telephone', models.CharField(db_column='TELEPHONE', max_length=14)),
                ('phone_number', models.CharField(blank=True, db_column='PHONE_NUMBER', max_length=15)),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'db_table': 'CUSTOMER',
            },
        ),
    ]