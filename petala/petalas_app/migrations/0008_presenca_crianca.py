# Generated by Django 4.2.5 on 2023-11-28 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petalas_app', '0007_presenca_remove_crianca_faltas_doacao_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenca',
            name='crianca',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='petalas_app.crianca'),
            preserve_default=False,
        ),
    ]