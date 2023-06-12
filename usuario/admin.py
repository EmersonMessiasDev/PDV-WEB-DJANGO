from django.contrib import admin
from .models import *

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'nome', 'cargo','esta_logado']

admin.site.register(Cargo)
