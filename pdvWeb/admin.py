from django.contrib import admin
from .models import *


class produtoEmLinha(admin.StackedInline):
    model = ItemVenda

class VendaAdmin(admin.ModelAdmin):
    inlines = [produtoEmLinha]
    readonly_fields = ['total']

admin.site.register(Produto)
admin.site.register(Venda, VendaAdmin)
admin.site.register(NotaFiscal)
