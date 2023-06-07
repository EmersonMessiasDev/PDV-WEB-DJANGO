from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from usuario.models import *

def home(request):
    try:
      usuario = request.session.get('usuario')
      request_usuario = Funcionario.objects.get(id = usuario ) 
      return render(request, 'home_pdv.html', {'usuario':request_usuario})
    except:
      return render(request, 'login.html')



def nova_venda(request):
    venda = Venda.objects.create(total=0)  # Cria uma nova venda com total 0
    return redirect('pdvWeb:adicionar_produto', venda_id=venda.id)  # Redireciona para a view 'adicionar_produto' com o id da venda


def adicionar_produto(request, venda_id):
    usuario = request.session.get('usuario')
    request_usuario = Funcionario.objects.get(id = usuario ) 
    
    if request.method == 'POST':
        codigo_produto = request.POST['codigo_produto']
        quantidade = int(request.POST['quantidade'])
        produto = Produto.objects.get(codigo=codigo_produto)
        
                
        item_venda = ItemVenda.objects.create(
            venda_id=venda_id,
            produto=produto,
            quantidade=quantidade,
            subtotal=produto.valor * quantidade
        )
        
        venda = Venda.objects.get(id=venda_id)
        venda.total += item_venda.subtotal
        venda.save()


    venda = Venda.objects.get(id=venda_id)
    itens_venda = ItemVenda.objects.filter(venda_id=venda_id)
    
    return render(request, 'venda_pdv.html', {'venda': venda, 'itens_venda': itens_venda, 'usuario':request_usuario})




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
  v_valor = request.POST.get('valor')
  v_valor =  v_valor.replace('R$', '')
  v_valor = v_valor.replace(',', '.')
  v_valor = float(v_valor)
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