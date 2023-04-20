from django.db import models

class Funcao(models.Model):
  nome = models.CharField(max_length=30)
  
  def __str__(self) -> str:
    return self.nome

class Funcionario(models.Model):
  cpf = models.CharField(max_length=11, null=False, blank=False)
  nome = models.CharField(max_length=50, null=False, blank=False)
  funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, null=False, blank=False)
  
  def __str__(self) -> str:
    return self.nome