from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('gerencia/', views.gerencia, name='gerencia'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
    
]