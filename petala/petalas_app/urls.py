from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('criancas/', views.listagem_crianca, name='listagem_criancas'),
    path('home/', views.home, name='home'),
    path('navbar/', views.navbar, name='navbar'),
]