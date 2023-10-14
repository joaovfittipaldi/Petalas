# Generated by Django 4.2.5 on 2023-10-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crianca',
            fields=[
                ('id_crianca', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('idade', models.IntegerField()),
                ('nascimento', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('periodo', models.TextField(max_length=255)),
                ('entrada', models.TextField(max_length=255)),
                ('permanencia', models.TextField(max_length=255)),
                ('turma', models.TextField(max_length=255)),
                ('autoavaliacao', models.TextField(max_length=255)),
                ('faltas', models.IntegerField()),
            ],
        ),
    ]