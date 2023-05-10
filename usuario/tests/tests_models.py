from django.test import TestCase
from ..models import Funcionario, Funcao

# Create your tests here.

class FuncaoTestCase(TestCase):
    
    
    def setUp(self):
        Funcao.objects.create(nome='Gerente')


    def test_funcao_criada(self):
        funcao = Funcao.objects.get(nome='Gerente')
        self.assertEqual(funcao.nome, 'Gerente')
        
   
        

class FuncionarioTestCase(TestCase):
    
    
    def setUp(self):
        funcao = Funcao.objects.create(nome='Gerente')
        Funcionario.objects.create(cpf='123.123.123-12', nome='Emerson', funcao=funcao)
        
    def test_funcionario_criado(self):
        funcionario = Funcionario.objects.get(cpf='123.123.123-12')
        self.assertEqual(funcionario.nome, 'Emerson')
        self.assertEqual(funcionario.funcao.nome, 'Gerente')