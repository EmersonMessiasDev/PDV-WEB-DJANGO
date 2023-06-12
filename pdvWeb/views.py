from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from usuario.models import *
from django.http import JsonResponse
from django.contrib.messages import constants
from django.contrib import messages
from django.utils import timezone
from .utils import *

#---------------------------------------------------------------------------------------------------
# todo                                      Renderização de paginas
#---------------------------------------------------------------------------------------------------
def home(request):
    try:
      venda_aberta = Venda.objects.filter(finalizada=False)
      usuario = request.session.get('usuario')
      request_usuario = Funcionario.objects.get(id = usuario ) 
      return render(request, 'home_pdv.html', {'venda_aberta':venda_aberta,'usuario':request_usuario})
    except:
      return render(request, 'login.html')


def produtos(request):
    produtos = Produto.objects.all()
    usuario = request.session.get('usuario')
    request_usuario = Funcionario.objects.get(id = usuario )
    
    return render(request, 'lista_produtos.html', {'produtos': produtos,'usuario':request_usuario})


def todos_produtos(request):
    produtos = Produto.objects.all().values('codigo', 'descricao', 'valor', 'quantidade')
    produtos_list = list(produtos)  
    return JsonResponse(produtos_list, safe=False)
  
  
#---------------------------------------------------------------------------------------------------
# todo                                      Funções de admin
#---------------------------------------------------------------------------------------------------
def cadastrar_produto(request):
  if request.session.get('usuario'):  
    v_codigo = int(request.POST.get('codigo'))
    v_descricao = request.POST.get('descricao')
    v_valor = float(request.POST.get('valor'))
    v_quantidade = int(request.POST.get('quantidade'))
    
    produto = Produto.objects.filter(codigo = v_codigo)
    if produto.exists():
      messages.error(request, 'ERROR! Código do produto já existe!')
      return redirect('pdvWeb:produtos')
    
    Produto.objects.create(codigo = v_codigo, descricao = v_descricao, valor = v_valor, quantidade = v_quantidade)
    messages.success(request, 'Produto cadastrado com sucesso!')
    return redirect('pdvWeb:produtos')
  else:
      messages.add_message(request, constants.ERROR, 'Usuario não está logado!')
      return redirect('usuario:login')


def atualizar_produto(request, id):
    produto = Produto.objects.get(id = id)
    v_codigo = int(request.POST.get('codigo'))
    v_descricao = request.POST.get('descricao')
    v_valor = request.POST.get('valor')
    v_valor =  v_valor.replace('R$', '')
    v_valor = v_valor.replace(',', '.')
    v_valor = float(v_valor)
    v_quantidade = int(request.POST.get('quantidade'))
    
    if not validar_produto(request, v_codigo, v_descricao, v_valor, v_quantidade ):
        messages.add_message(request, messages.ERROR, 'DEU MERDA!')
        return redirect('pdvWeb:produtos')
    
    
    produto.descricao = v_descricao
    produto.valor = v_valor
    produto.quantidade = v_quantidade
    produto.save()
    
    messages.add_message(request, messages.SUCCESS, 'Produto atualizado com sucesso!')
    return redirect('pdvWeb:produtos')
  

def deletar_produto(request, id):
  produto = Produto.objects.get(id = id)
  
  produto.delete()
  
  return redirect('pdvWeb:produtos') 


def personalizar(request):
    if request.session.get('usuario'): 
      usuario = request.session.get('usuario')
      request_usuario = Funcionario.objects.get(id = usuario )
      return render(request, 'configuracoes.html',{'usuario':request_usuario})
    else:
      messages.add_message(request, constants.ERROR, 'Usuario não está logado!')
      return redirect('usuario:login')
#---------------------------------------------------------------------------------------------------
# todo                                      Funções de venda
#---------------------------------------------------------------------------------------------------

def format_cpf(value):
    return "%s.%s.%s-%s" % (value[0:3], value[3:6], value[6:9], value[9:11])
  
  
def nova_venda(request):
    print(timezone.now())
    try:
      cpf = request.POST.get('cpf')
      venda = Venda.objects.create(total=0, cpf_cliente=cpf, data = timezone.now().strftime("%d-%m-%Y %H:%M:%S"))# Cria uma nova venda com total 0
    except:
      venda = Venda.objects.create(total=0, data = timezone.now().strftime("%d-%m-%Y %H:%M:%S"))# Cria uma nova venda com total 0
    return redirect('pdvWeb:adicionar_produto', venda_id=venda.id)  # Redireciona para a view 'adicionar_produto' com o id da venda


def retornar_venda(request, id):
    try:
        venda = Venda.objects.get(id=id)  # substitua 'Venda' pela classe do seu modelo de venda
    except Venda.DoesNotExist:
        # Redireciona para a página inicial, por exemplo, se a venda não existe
        return redirect('nome_da_sua_url_home')
        
    context = {'venda': venda}
    return render(request, 'venda_pdv.html', context)


def adicionar_produto(request, venda_id):
    usuario = request.session.get('usuario')
    request_usuario = Funcionario.objects.get(id = usuario ) 
    todos_produtos = Produto.objects.all()
    
    venda_aberta = Venda.objects.filter(finalizada=False)
    
    if request.method == 'POST':
        codigo_produto = request.POST['codigo_produto']
        quantidade = request.POST['quantidade']
        if quantidade.strip() == '' or codigo_produto.strip() == '':
          messages.add_message(request, constants.SUCCESS, 'quantidade não pode ser vazio!')
          return redirect('pdvWeb:adicionar_produto', venda_id)
        
        try:
          quantidade = int(quantidade)
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
        except:
          messages.add_message(request, constants.SUCCESS, 'Codigo do produto invalido!')
          return redirect('pdvWeb:adicionar_produto', venda_id)
          


    venda = Venda.objects.get(id=venda_id)
    itens_venda = ItemVenda.objects.filter(venda_id=venda_id)
    
    return render(request, 'venda_pdv.html', {'venda_aberta':venda_aberta, 'venda': venda, 'itens_venda': itens_venda, 'usuario':request_usuario, 'todos_produtos':todos_produtos})


def buscar_produto(request):
    codigo = request.GET.get('codigo', None)
    try:
        produto = Produto.objects.get(codigo=codigo)
        data = {'produto': {
            'codigo': produto.codigo,
            'descricao': produto.descricao,
            'valor': produto.valor,
            'quantidade': produto.quantidade
        }}
    except Produto.DoesNotExist:
        data = {'produto': None}
    return JsonResponse(data)


def deletar_item_venda(request, id):
      if request.method == 'POST':
        cpf = request.POST.get('cpf')
        
        usuario = Funcionario.objects.filter(cpf = cpf).filter(cargo = 2)
        
        produto = ItemVenda.objects.get(id = id)
        
        if len(usuario) == 0:
          messages.add_message(request, constants.ERROR, 'Matricula invalida!')
          return redirect('pdvWeb:adicionar_produto', produto.venda.id)
        
        
        produto.delete()
        
        produto.venda.total -= produto.subtotal
        produto.venda.save()
        messages.add_message(request, constants.SUCCESS, 'Item deletado com sucesso!')
        return redirect('pdvWeb:adicionar_produto', produto.venda.id) 


def cancelar_venda(request, id):
  if request.method == 'POST':
        cpf = request.POST.get('cpf')
        
        usuario = Funcionario.objects.filter(cpf = cpf).filter(cargo = 2)
        
        venda = Venda.objects.get(id = id)
        
        if len(usuario) == 0:
          messages.add_message(request, constants.ERROR, 'Matricula invalida!')
          return redirect('pdvWeb:adicionar_produto' , venda.id)
  
  venda = Venda.objects.get(id = id)
  
  venda.delete()
  
  messages.add_message(request, constants.SUCCESS, 'Venda cancelada!')
  return redirect('pdvWeb:home') 


def finalizar_venda(request, id):
    usuario = request.session.get('usuario')
    request_usuario = Funcionario.objects.get(id = usuario ) 
    if request.method == 'POST':
      recebido = request.POST.get('recebido')
      venda = Venda.objects.get(id=id)
      
      nota_fiscal = NotaFiscal(funcionario=request_usuario, venda=venda, total = venda.total)
      nota_fiscal.save()
      
      venda.finalizada = True
      venda.save()
            
      
      # formatar o CPF
      cpf_cliente = format_cpf(venda.cpf_cliente)
      itens = ItemVenda.objects.filter(venda=venda)
      for i in itens:
        i.produto.quantidade -= i.quantidade
        i.produto.save()
        
      troco = float(recebido) - float(venda.total)
      context = {'recebido':recebido,
                 'troco':troco,
                 'itens':itens,
                 'venda':venda,
                 'nota_fiscal':nota_fiscal,
                 'cpf_cliente': cpf_cliente
                 }
      
      return render(request, 'notaFiscal.html', context)
    
    