# Generated by Django 4.0.6 on 2022-08-04 19:46

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
            name='MonthlyModel',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_initial', models.DateField(db_column='DATE_INITIAL')),
                ('date_final', models.DateField(db_column='DATE_FINAL')),
                ('value_money', models.FloatField(db_column='VALUE_MONEY')),
                ('amount_paid', models.FloatField(db_column='AMOUNT_PAID')),
                ('scheduling_amount', models.PositiveIntegerField(db_column='SCHEDULING_AMOUNT')),
                ('animal', models.ForeignKey(db_column='ANIMAL', on_delete=django.db.models.deletion.CASCADE, to='animal.animalmodel')),
            ],
            options={
                'verbose_name': 'monthly',
                'verbose_name_plural': 'monthlies',
                'db_table': 'MONTHLY',
            },
        ),
    ]
