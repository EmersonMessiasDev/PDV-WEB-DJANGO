from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from hashlib import sha256, sha1
from django.contrib.messages import constants
from django.contrib import messages

def cadastro(request):
  cargos = Cargo.objects.all()
  
  return render(request, 'cadastro.html', {'cargos': cargos})



def funcionarios(request):
  funcionarios = Funcionario.objects.all()
  
  return render(request, 'funcionarios.html', {'funcionarios': funcionarios})



def login(request):
  return render(request, 'login.html')

def validar_login(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    
    
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

      



def sair(request):
    messages.add_message(request, constants.SUCCESS, 'Você saiu do portal!')
    request.session.flush()
    return redirect('usuario:login')


def gerencia(request):
  return render(request, 'gerencia.html')



def cadastrar_funcionario(request):
  v_nome = request.POST.get('nome')
  v_cpf = request.POST.get('cpf')
  v_cargo = request.POST.get('cargo')
  cargo = Cargo.objects.get(id = v_cargo)
  
  Funcionario.objects.create(nome = v_nome, cpf = v_cpf, cargo = cargo)
  
  return redirect('usuario:funcionarios')



def atualizando_funcionario(request, id):
  funcionario = Funcionario.objects.get(id = id)
  cargos = Cargo.objects.all()
  
  return render(request, 'atualizando_funcionario.html', {'funcionario': funcionario,
                                                   'cargos': cargos})
  
  
  
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
  
  return redirect('usuario:funcionarios')



def deletar_funcionario(request, id):
  funcionario = Funcionario.objects.get(id = id)
  
  funcionario.delete()
  return redirect('usuario:funcionarios')
  