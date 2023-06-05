from django.db import models
from usuario.models import Funcionario

class Produto(models.Model):
  codigo = models.IntegerField(null=False, blank=False)
  descricao = models.CharField(max_length=50, null=False, blank=False)
  valor = models.FloatField(null=False, blank=False)
  quantidade = models.IntegerField(null=False, blank=False)
  
  def __str__(self) -> str:
    return self.descricao
  
class Venda(models.Model):
    produtos = models.ManyToManyField(Produto, through='ItemVenda')
    total = models.FloatField(null=False, blank=False)
    

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False)
    subtotal = models.FloatField(null=False, blank=False)
  
  
class NotaFiscal(models.Model):
  funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING, null=False, blank=False)
  venda = models.ForeignKey(Venda, on_delete=models.DO_NOTHING, null=False, blank=False)
  total = models.FloatField(null=False, blank=False)