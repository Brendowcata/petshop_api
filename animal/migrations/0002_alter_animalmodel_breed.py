# Generated by Django 4.0.6 on 2022-08-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalmodel',
            name='breed',
            field=models.CharField(choices=[('Teste', 'Teste')], db_column='BREED', max_length=30),
        ),
    ]
