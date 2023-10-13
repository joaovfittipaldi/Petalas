from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('criancas/', views.listagem_crianca, name='listagem_criancas'),
    path('cadastro_crianca/', views.cadastro_crianca, name='cadastro_crianca'),
    path('navbar/', views.navbar, name='navbar'),
]