from django.db import models

# Create your models here.

class Crianca(models.Model):
    id_crianca = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    nascimento = models.DateField()
    status = models.TextField(max_length=255)
    periodo = models.TextField(max_length=255)
    entrada = models.DateField()
    permanencia = models.TextField(max_length=255)
    turma = models.TextField(max_length=255)
    autoavaliacao = models.TextField(max_length=255)

class Doacao(models.Model):
    id_doacao = models.AutoField(primary_key=True)
    nome_padrinho = models.TextField(max_length=255)
    cpf = models.IntegerField()
    valor = models.IntegerField()
    nome_crianca = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)

class Presenca(models.Model):
    id_presenca = models.AutoField(primary_key=True)
    data = models.DateField()
    turma = models.TextField(max_length=255)
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    presentes = models.BooleanField(default=False)
