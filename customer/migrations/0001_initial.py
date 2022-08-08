# Generated by Django 4.0.6 on 2022-08-08 20:26

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_column='EXTERNAL_ID', default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(db_column='NAME', max_length=150)),
                ('cpf', models.CharField(db_column='CPF', max_length=14, unique=True)),
                ('birth_date', models.DateField(blank=True, db_column='BIRTH_DATE', null=True)),
                ('email', models.EmailField(blank=True, db_column='EMAIL', max_length=254, null=True)),
                ('telephone', models.CharField(blank=True, db_column='TELEPHONE', max_length=14, null=True)),
                ('phone_number', models.CharField(db_column='PHONE_NUMBER', max_length=15)),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'db_table': 'CUSTOMER',
            },
        ),
    ]
