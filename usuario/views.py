from django.shortcuts import render, redirect
from django.http import HttpResponse

def cadastro(request):
  return render(request, 'cadastro.html')

def funcionarios(request):
  return render(request, 'funcionarios.html')

def login(request):
  return render(request, 'login.html')

def gerencia(request):
  return render(request, 'gerencia.html')


