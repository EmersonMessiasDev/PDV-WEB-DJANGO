from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

def home(request):
  return render(request, 'home_pdv.html')

def produtos(request):
  produtos = Produto.objects.all()
  
  return render(request, 'lista_produtos.html', {'produtos': produtos})

def cadastro_produto(request):
  return render(request, 'cadastro_produto.html')

def atualizacao_produto(request, id):
  produto = Produto.objects.get(id = id)
  
  return render(request, 'atualizacao_produto.html', {'produto': produto})

def cadastrar_produto(request):
  v_codigo = request.POST.get('codigo')
  v_descricao = request.POST.get('descricao')
  v_valor = request.POST.get('valor')
  v_quantidade = request.POST.get('quantidade')
  
  Produto.objects.create(codigo = v_codigo, nome = v_descricao, valor = v_valor, estoque = v_quantidade)
  
  return redirect('pdvWeb:produtos')

def atualizar_produto(request, id):
  v_codigo = request.POST.get('codigo')
  v_descricao = request.POST.get('descricao')
  v_valor = request.POST.get('valor')
  v_quantidade = request.POST.get('quantidade')
  
  produto = Produto.objects.get(id = id)
  
  produto.codigo = v_codigo
  produto.nome = v_descricao
  produto.valor = v_valor
  produto.estoque = v_quantidade
  produto.save()
  
  return redirect('pdvWeb:produtos')

def deletar_produto(request, id):
  produto = Produto.objects.get(id = id)
  
  produto.delete()
  
  return redirect('pdvWeb:produtos')  