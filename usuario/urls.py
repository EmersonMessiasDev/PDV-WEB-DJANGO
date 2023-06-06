from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

app_name = 'usuario'

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('gerencia/', gerencia, name='gerencia'),
    path('funcionarios/', funcionarios, name='funcionarios'),
    path('cadastrar_funcionario/', cadastrar_funcionario, name='cadastrar_funcionario'),
    path('atualizando_funcionario/<int:id>', atualizando_funcionario, name='atualizando_funcionario'),
    path('atualizar_funcionario/<int:id>', atualizar_funcionario, name='atualizar_funcionario'),
    path('deletar_funcionario/<int:id>', deletar_funcionario, name='deletar_funcionario'),
    path('validar_login/', validar_login, name='validar_login' ),
    path('sair/', sair, name='sair')
    
]