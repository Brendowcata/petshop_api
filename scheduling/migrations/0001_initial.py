# Generated by Django 4.0.6 on 2022-08-04 18:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchedulingModel',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bath', models.BooleanField(db_column='BATH', default=False)),
                ('clipping', models.CharField(blank=True, choices=[('SEM_SERVICO', 'Sem Serviço'), ('TOSA_TESOURA', 'Tosa na Tesoura'), ('TOSA_MAQUINA', 'Tosa na Máquina'), ('TOSA_BEBE', 'Tosa Bebê'), ('TOSA_RACA', 'Tosa de Raça'), ('TOSA_VERAO', 'Tosa Verão'), ('TOSA_HIGIENICA', 'Tosa Higiênica'), ('TOSA_ESTETICA', 'Tosa Estética')], db_column='TYPE_CLIPPING', max_length=15, null=True)),
                ('hydration', models.BooleanField(db_column='HYDRATION', default=False)),
                ('clearance', models.BooleanField(db_column='CLEARANCE', default=False)),
                ('dyeing', models.CharField(blank=True, choices=[('SEM_SERVICO', 'Sem Serviço'), ('VERMELHO', 'Vermelho'), ('AMARELO', 'Amarelo'), ('AZUL', 'Azul'), ('VERDE', 'Verde'), ('LARANJA', 'Laranja'), ('ROXO', 'Roxo'), ('ROSA', 'Rosa'), ('BRANCO', 'Branco'), ('PRETO', 'Preto'), ('MARROM', 'Marrom'), ('CINZA', 'Cinza'), ('DOURADO', 'Dourado')], db_column='DYEING', max_length=11, null=True)),
                ('brush_teeth', models.BooleanField(db_column='BRUSH_TEETH', default=False)),
                ('cut_nails', models.BooleanField(db_column='CUT_NAILS', default=False)),
                ('transport', models.BooleanField(db_column='TRANSPORT', default=False)),
                ('date_appointment', models.DateField(db_column='DATE_SCHEDULING')),
                ('hour_appointment', models.TimeField(db_column='HOUR_APPOINTMENT')),
                ('value_money', models.FloatField(db_column='VALUE_MONEY')),
                ('amount_paid', models.FloatField(db_column='AMOUNT_PAID')),
                ('animal', models.ForeignKey(db_column='ANIMAL', on_delete=django.db.models.deletion.CASCADE, to='animal.animalmodel')),
            ],
            options={
                'verbose_name': 'scheduling',
                'verbose_name_plural': 'schedules',
                'db_table': 'SCHEDULING',
            },
        ),
    ]
