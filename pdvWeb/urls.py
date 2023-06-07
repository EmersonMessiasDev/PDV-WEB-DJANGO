from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

app_name = 'pdvWeb'

urlpatterns = [
    path('', home, name='home'),
    path('produtos/', produtos, name='produtos'),
    path('cadastro_produto/', cadastro_produto, name='cadastro_produto'),
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
    path('atualizacao_produto/<int:id>', atualizacao_produto, name='atualizacao_produto'),
    path('atualizar_produto/<int:id>', atualizar_produto, name='atualizar_produto'),
    path('deletar_produto/<int:id>', deletar_produto, name='deletar_produto'),
    path('nova_venda/', nova_venda, name='nova_venda'),
    path('venda/<int:venda_id>/', adicionar_produto, name='adicionar_produto')
    
]