from django.shortcuts import render, redirect
from .models import Crianca

# Create your views here.

def home(request):
    return render(request, 'cadastro_crianca.html')

def listagem_crianca(request):
    if request.method == "POST":
        nova_crianca = Crianca()
        nova_crianca.nome = request.POST.get('nome')
        nova_crianca.idade = request.POST.get('idade')
        nova_crianca.nascimento = request.POST.get('nascimento')
        nova_crianca.status = request.POST.get('status')
        nova_crianca.periodo = request.POST.get('periodo')
        nova_crianca.entrada = request.POST.get('entrada')
        nova_crianca.permanencia = request.POST.get('permanencia')
        nova_crianca.turma = request.POST.get('turma')
        nova_crianca.autoavaliacao = request.POST.get('autoavaliacao')
        nova_crianca.faltas = request.POST.get('faltas')
        nova_crianca.save()

    criancas = {
        'criancas': Crianca.objects.all()
    }

    return render(request, 'criancas.html', criancas)

def home(request):
    return render(request, 'home.html')

def navbar(request):
    return render(request, 'navbar.html')
