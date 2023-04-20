from django.db import models
from usuario.models import Funcionario

class Produto(models.Model):
  codigo = models.IntegerField(null=False, blank=False)
  nome = models.CharField(max_length=50, null=False, blank=False)
  valor = models.FloatField(null=False, blank=False)
  estoque = models.IntegerField(null=False, blank=False)
  
  def __str__(self) -> str:
    return self.nome
  
class Venda(models.Model):
  produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING, null=False, blank=False)
  qtd = models.IntegerField(null=False, blank=False)
  total = models.FloatField(null=False, blank=False)
  
class NotaFiscal(models.Model):
  funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING, null=False, blank=False)
  venda = models.ForeignKey(Venda, on_delete=models.DO_NOTHING, null=False, blank=False)
  total = models.FloatField(null=False, blank=False)