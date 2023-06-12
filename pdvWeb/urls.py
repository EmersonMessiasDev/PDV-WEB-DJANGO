from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

app_name = 'pdvWeb'

urlpatterns = [
    path('', home, name='home'),
    path('produtos/', produtos, name='produtos'),
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
    path('atualizar_produto/<int:id>', atualizar_produto, name='atualizar_produto'),
    path('deletar_produto/<int:id>', deletar_produto, name='deletar_produto'),
    path('deletar_item_venda/<int:id>', deletar_item_venda, name='deletar_item_venda'),
    path('nova_venda/', nova_venda, name='nova_venda'),
    path('venda/<int:venda_id>/', adicionar_produto, name='adicionar_produto'),
    path('todos_produtos/', todos_produtos, name='todos_produtos'),
    path('buscar_produto/', buscar_produto, name='buscar_produto'),
    path('finalizar_venda/<int:id>', finalizar_venda, name='finalizar_venda'),
    path('retornar_venda/<int:id>', retornar_venda, name='retornar_venda'),
    path('cancelar_venda/<int:id>', cancelar_venda, name='cancelar_venda'),
    path('personalizar/', personalizar, name='personalizar')
    
]