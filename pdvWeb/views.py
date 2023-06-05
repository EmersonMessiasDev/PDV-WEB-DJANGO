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
  v_codigo = int(request.POST.get('codigo'))
  v_descricao = request.POST.get('descricao')
  v_valor = float(request.POST.get('valor'))
  v_quantidade = int(request.POST.get('quantidade'))
  
  Produto.objects.create(codigo = v_codigo, descricao = v_descricao, valor = v_valor, quantidade = v_quantidade)
  
  return redirect('pdvWeb:produtos')

def atualizar_produto(request, id):
  v_codigo = int(request.POST.get('codigo'))
  v_descricao = request.POST.get('descricao')
  v_valor = float(request.POST.get('valor'))
  v_quantidade = int(request.POST.get('quantidade'))
  
  produto = Produto.objects.get(id = id)
  
  if v_codigo > 0:
    produto.codigo = v_codigo
    if v_descricao != '':
      produto.descricao = v_descricao
      if v_valor > 0 and v_valor != '':
        produto.valor = v_valor
        if v_quantidade != '':
          produto.quantidade = v_quantidade
          produto.save()
          return redirect('pdvWeb:produtos')
        else:
          id_produto = produto.id
          return redirect('pdvWeb:atualizacao_produto', id_produto)
      else:
        id_produto = produto.id
        return redirect('pdvWeb:atualizacao_produto', id_produto)
    else:
      id_produto = produto.id
      return redirect('pdvWeb:atualizacao_produto', id_produto)
  else:
    id_produto = produto.id
    return redirect('pdvWeb:atualizacao_produto', id_produto)

def deletar_produto(request, id):
  produto = Produto.objects.get(id = id)
  
  produto.delete()
  
  return redirect('pdvWeb:produtos')  