from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from hashlib import sha256, sha1
from django.contrib.messages import constants
from django.contrib import messages
from pdvWeb.models import *
from django.db.models import Sum
import datetime

#---------------------------------------------------------------------------------------------------
# todo                                      Renderização de paginas
#---------------------------------------------------------------------------------------------------

def cadastro(request):
  cargos = Cargo.objects.all()
  
  return render(request, 'cadastro.html', {'cargos': cargos})


def login(request):
  return render(request, 'login.html')


def sair(request):
    messages.success(request,  'Você saiu do portal!')
    request.session.flush()
    return redirect('usuario:login')


def gerencia(request):
    usuario = request.session.get('usuario')
    request_usuario = Funcionario.objects.get(id = usuario ) 
    return render(request, 'gerencia.html', {'usuario':request_usuario})


def funcionarios(request):
  funcionarios = Funcionario.objects.all()
  usuario = request.session.get('usuario')
  request_usuario = Funcionario.objects.get(id = usuario )
  cargos = Cargo.objects.all()
  
  return render(request, 'funcionarios.html', {'cargos':cargos,'funcionarios': funcionarios,'usuario':request_usuario})


#---------------------------------------------------------------------------------------------------
# todo                                      Renderização de admin
#---------------------------------------------------------------------------------------------------

def validar_login(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    
    print(nome)
    print(cpf)
    
    
    try:
        funcionario = Funcionario.objects.get(nome=nome, cpf=cpf)
    except Funcionario.DoesNotExist:
        messages.add_message(request, constants.ERROR, 'Nome ou CPF inválidos!')
        return redirect('usuario:login')

    if funcionario.cargo.nome == 'Gerente':  
      messages.add_message(request, constants.SUCCESS, 'Gerente logado com sucesso!')
      request.session['usuario'] = funcionario.id
      return redirect('usuario:gerencia')
    else: 
      messages.add_message(request, constants.SUCCESS, 'Funcionario logado com sucesso!')
      request.session['usuario'] = funcionario.id
      return redirect('pdvWeb:home')

      
def vendas(request):
    usuario = request.session.get('usuario')
    request_usuario = Funcionario.objects.get(id = usuario ) 
    total_venda = NotaFiscal.objects.all()
    valor_bruto_vendas = NotaFiscal.objects.aggregate(Sum('total'))['total__sum']
    ticket_medio = valor_bruto_vendas / len(total_venda)
    ranking_funcionarios = (
    NotaFiscal.objects.values('funcionario__nome')  # Agrupa por nome do funcionário
    .annotate(vendas_total=Sum('total'))  # Soma o total de cada grupo
    .order_by('-vendas_total')  # Ordena em ordem decrescente pelo total de vendas
    )    
    
    top_vendedor = ranking_funcionarios.first()
    top_vendedor = top_vendedor['funcionario__nome']
    # Obter a data atual
    data_atual = timezone.now().date()

    # Consulta para obter o total de vendas do dia atual
    vendas_dia = Venda.objects.filter(data__startswith=data_atual.strftime('%d-%m-%Y'), finalizada=True).aggregate(total_vendas=Sum('total'))['total_vendas']
    historico_venda = Venda.objects.filter(data__startswith=data_atual.strftime('%d-%m-%Y'), finalizada=True)

    vendas = []
    for venda in historico_venda:
        notas_fiscais = NotaFiscal.objects.filter(venda=venda)
        for nota_fiscal in notas_fiscais:
            vendas.append({
                'total': venda.total,
                'funcionario': nota_fiscal.funcionario.nome,
                'data_venda': venda.data
            })

    # Pega todos os produtos com quantidade em estoque abaixo de 100
    produtos_estoque_baixo = Produto.objects.filter(quantidade__lt=100)

    # Pega os 5 produtos mais vendidos
    produtos_mais_vendidos = ItemVenda.objects.values('produto__codigo', 'produto__descricao').annotate(total_vendido=Sum('quantidade')).order_by('-total_vendido')[:5]

    # Recupera os produtos usando os ids obtidos da consulta acima

    # Pega a quantidade vendida do produto mais vendido
    print(produtos_mais_vendidos)
    context ={
      'usuario':request_usuario,
      'total_venda':total_venda,
      'valor_bruto':valor_bruto_vendas,
      'ticket_medio':ticket_medio,
      'ranking':ranking_funcionarios,
      'top_vendedor':top_vendedor,
      'vendas_dia':vendas_dia,
      'historico_venda':vendas,
      'produto_mais_vendido':produtos_mais_vendidos,
      'estoque_baixo':produtos_estoque_baixo,
      }
    
    return render(request, 'vendas.html', context)


def cadastrar_funcionario(request):
  v_nome = request.POST.get('nome')
  v_cpf = request.POST.get('cpf')
  v_cargo = request.POST.get('cargo')
  cargo = Cargo.objects.get(id = v_cargo)
  
  funcionario = Funcionario.objects.filter(cpf=v_cpf)
  if funcionario.exists():
     messages.error(request,  'ERROR! CPF já está cadastrado!')
     return redirect('usuario:funcionarios')
  
  Funcionario.objects.create(nome = v_nome, cpf = v_cpf, cargo = cargo)
  
  messages.success(request,  'Funcionario cadastrado com sucesso!')
  return redirect('usuario:funcionarios')
  
  
def atualizar_funcionario(request, id):
  funcionario = Funcionario.objects.get(id = id)
  
  v_nome = request.POST.get('nome')
  v_cpf = request.POST.get('cpf')
  v_cargo = request.POST.get('cargo')
  cargo = Cargo.objects.get(id = v_cargo)
  
  funcionario.nome = v_nome
  funcionario.cpf = v_cpf
  funcionario.cargo = cargo
  
  funcionario.save()
  messages.add_message(request, constants.SUCCESS, 'Funcionario atualizado com sucesso!')
  return redirect('usuario:funcionarios')


def deletar_funcionario(request, id):
  funcionario = Funcionario.objects.get(id = id)
  
  funcionario.delete()
  messages.add_message(request, constants.SUCCESS, 'Funcionario excluido com sucesso!')
  return redirect('usuario:funcionarios')
  