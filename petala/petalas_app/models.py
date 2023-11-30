from django.db import models

# Create your models here.

class Crianca(models.Model):
    id_crianca = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    nascimento = models.DateField()
    entrada = models.DateField()
    turma = models.TextField(max_length=255)
    cpf_crianca = models.TextField(max_length=255)
    nome_resp = models.TextField(max_length=255)
    email_resp = models.TextField(max_length=255)
    tel_resp = models.TextField(max_length=255)
    cpf_resp = models.TextField(max_length=255)

class Doacao(models.Model):
    id_doacao = models.AutoField(primary_key=True)
    nome_padrinho = models.TextField(max_length=255)
    cpf = models.TextField(max_length=255)
    valor = models.IntegerField()
    destino = models.TextField(max_length=255)
    tipo= models.TextField(max_length=255)

class Presenca(models.Model):
    id_presenca = models.AutoField(primary_key=True)
    data = models.DateField()
    turma = models.TextField(max_length=255)
    crianca_nome = models.TextField()
    presentes = models.BooleanField(default=False)
