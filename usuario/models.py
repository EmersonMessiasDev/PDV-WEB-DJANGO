from django.db import models

class Cargo(models.Model):
  nome = models.CharField(max_length=30)
  
  def __str__(self) -> str:
    return self.nome


class Funcionario(models.Model):
  cpf = models.CharField(max_length=11, null=False, blank=False)
  nome = models.CharField(max_length=50, null=False, blank=False)
  cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=False, blank=False)
  esta_logado = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return self.nome