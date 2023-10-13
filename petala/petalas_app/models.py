from django.db import models

# Create your models here.

class Crianca(models.Model):
    id_crianca = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    nascimento = models.DateTimeField()
    status = models.TextField(max_length=255)
    periodo = models.TextField(max_length=255)
    entrada = models.DateTimeField()
    permanencia = models.TextField(max_length=255)
    turma = models.TextField(max_length=255)
    autoavaliacao = models.TextField(max_length=255)
    faltas = models.IntegerField()
