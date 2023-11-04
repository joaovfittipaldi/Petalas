from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criancas/', views.listagem_crianca, name='listagem_criancas'),
    path('cadastro_crianca/', views.cadastro_crianca, name='cadastro_crianca'),
    path('info_crianca/<int:crianca_id>/', views.info_crianca, name='info_crianca'),
    path('navbar/', views.navbar, name='navbar'),
    path('cadastro_doacao/', views.cadastro_doacao, name='cadastro_doacao'),
    path('info_doacao/<int:doacao_id>/', views.info_doacao, name='info_doacao'),
    path('doacoes/', views.listagem_doacao, name='listagem_doacoes')
]