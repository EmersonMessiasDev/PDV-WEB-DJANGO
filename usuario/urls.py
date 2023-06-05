from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('gerencia/', views.gerencia, name='gerencia'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('atualizando_funcionario/<int:id>', views.atualizando_funcionario, name='atualizando_funcionario'),
    path('atualizar_funcionario/<int:id>', views.atualizar_funcionario, name='atualizar_funcionario'),
    path('deletar_funcionario/<int:id>', views.deletar_funcionario, name='deletar_funcionario'),
    
]