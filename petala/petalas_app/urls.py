from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('turmas/', views.listagem_turmas, name='listagem_turmas'),
    path('criancas/<str:turma_atual>/', views.listagem_crianca, name='listagem_criancas'),
    path('cadastro_crianca/<str:turma_atual>/', views.cadastro_crianca, name='cadastro_crianca'),
    path('info_crianca/<int:crianca_id>/', views.info_crianca, name='info_crianca'),
    path('navbar/', views.navbar, name='navbar'),
    path('cadastro_doacao/', views.cadastro_doacao, name='cadastro_doacao'),
    path('info_doacao/<int:doacao_id>/', views.info_doacao, name='info_doacao'),
    path('doacoes/', views.listagem_doacao, name='listagem_doacoes'),
    path('resultado_pesquisa/', views.resultado_pesquisa, name='resultado_pesquisa'),
    path('acesso/crianca/<int:id_field>/', views.acesso_crianca, name='acesso_crianca'),
    path('acesso/doacao/<int:id_field>/', views.acesso_doacao, name='acesso_doacao'),
    path('presencas/<str:turma_atual>/', views.listagem_presenca, name='listagem_presencas'),
    path('presenca/cadastro/<str:turma_atual>/', views.cadastro_presenca, name='cadastro_presenca'),
    path('presenca/info/<int:presenca_id>/', views.info_presenca, name='info_presenca'),
]