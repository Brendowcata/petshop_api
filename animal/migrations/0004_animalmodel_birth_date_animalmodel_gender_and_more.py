# Generated by Django 4.0.6 on 2022-08-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_alter_animalmodel_breed'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalmodel',
            name='birth_date',
            field=models.DateField(blank=True, db_column='BIRTH_DATE', null=True),
        ),
        migrations.AddField(
            model_name='animalmodel',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='GENDER', default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animalmodel',
            name='color',
            field=models.CharField(choices=[('ALBINO', 'Albino'), ('AMARELO', 'Amarelo'), ('AZUL', 'Azul'), ('BRANCO', 'Branco'), ('CINZA', 'Cinza'), ('DOURADO', 'Dourado'), ('PRETO', 'Preto'), ('MARROM', 'Marrom'), ('VERMELHO', 'Vermelho'), ('PRETO_BRANCO', 'Preto/Branco')], db_column='COLOR', max_length=15),
        ),
        migrations.AlterField(
            model_name='animalmodel',
            name='size',
            field=models.CharField(choices=[('PEQUENO', 'Pequeno'), ('MEDIO', 'Médio'), ('GRANDE', 'Grande')], db_column='SIZE', max_length=7),
        ),
    ]
