# Generated by Django 4.0.6 on 2022-10-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmodel',
            name='is_paid',
        ),
    ]