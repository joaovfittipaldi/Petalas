# Generated by Django 4.2 on 2023-11-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petalas_app', '0015_crianca_cpf_crianca_crianca_cpf_resp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crianca',
            name='cpf_crianca',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='cpf_resp',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='crianca',
            name='tel_resp',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='cpf',
            field=models.TextField(max_length=255),
        ),
    ]
