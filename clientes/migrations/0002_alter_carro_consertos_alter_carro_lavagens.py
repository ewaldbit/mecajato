# Generated by Django 5.1.3 on 2024-12-03 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='consertos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='lavagens',
            field=models.IntegerField(null=True),
        ),
    ]
