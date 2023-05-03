from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'pdvWeb'

urlpatterns = [
    path('', views.pdvWeb, name='pdvWeb'),
    path('produtos/', views.produtos, name='produtos'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
]