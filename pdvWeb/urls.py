from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'pdvWeb'

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('atualizacao_produto/<int:id>', views.atualizacao_produto, name='atualizacao_produto'),
    path('atualizar_produto/<int:id>', views.atualizar_produto, name='atualizar_produto'),
    path('deletar_produto/<int:id>', views.deletar_produto, name='deletar_produto'),
    
]