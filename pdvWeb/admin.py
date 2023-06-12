from django.contrib import admin
from .models import *


class produtoEmLinha(admin.StackedInline):
    model = ItemVenda

class VendaAdmin(admin.ModelAdmin):
    inlines = [produtoEmLinha]
    readonly_fields = ['total']
    list_display = ['valor_formatado', 'data', 'finalizada']
    
    def valor_formatado(self, obj):
        return "R$ {:.2f}".format(obj.total)
    valor_formatado.short_description = 'Valor'


@admin.register(CustomStore)
class CustomStoreAdmin(admin.ModelAdmin):
    list_display = ['nome']
    
@admin.register(NotaFiscal)
class NotaFiscAdmin(admin.ModelAdmin):
    readonly_fields = ['funcionario','venda','valor_formatado']
    list_display = ['venda','funcionario','valor_formatado']
    
    def valor_formatado(self, obj):
        return "R$ {:.2f}".format(obj.total)
    valor_formatado.short_description = 'Valor'


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'descricao', 'valor_formatado', 'quantidade']

    def valor_formatado(self, obj):
        return "R$ {:.2f}".format(obj.valor)
    valor_formatado.short_description = 'Valor'


admin.site.register(Venda, VendaAdmin)
