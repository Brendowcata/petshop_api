# Generated by Django 4.0.6 on 2022-08-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='cpf',
            field=models.CharField(db_column='CPF', max_length=14, unique=True),
        ),
    ]
