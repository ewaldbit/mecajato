# Generated by Django 5.1.3 on 2024-12-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicos',
            name='protocolo',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
