# Generated by Django 4.2 on 2023-10-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petalas_app', '0002_alter_crianca_entrada_alter_crianca_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crianca',
            name='entrada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='nascimento',
            field=models.DateField(),
        ),
    ]