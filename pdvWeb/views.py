from django.shortcuts import render, redirect
from django.http import HttpResponse

def pdvWeb(request):
  return render(request, 'home_pdv.html')

def produtos(request):
  return render(request, 'lista_produtos.html')

def cadastro_produto(request):
  return render(request, 'cadastro_produto.html')
