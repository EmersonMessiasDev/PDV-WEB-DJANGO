from django.test import TestCase
from ..models import Funcionario, Funcao

# Create your tests here.

class FuncionarioTestCase(TestCase):
    
    def test_criar_funcao(self):
        # Criar uma nova instância de "Funcao" com o nome "Gerente"
        funcao = Funcao.objects.create(nome='Gerente')

        # Verificar se a instância foi criada corretamente no banco de dados
        funcao_salva = Funcao.objects.get(id=funcao.id)
        self.assertEqual(funcao_salva.nome, 'Gerente')

    def test_atualizar_funcao(self):
        # Criar uma nova instância de "Funcao" com o nome "Assistente"
        funcao = Funcao.objects.create(nome='Assistente')

        # Atualizar o nome da função para "Auxiliar"
        funcao.nome = 'Auxiliar'
        funcao.save()

        # Verificar se a função foi atualizada corretamente no banco de dados
        funcao_atualizada = Funcao.objects.get(id=funcao.id)
        self.assertEqual(funcao_atualizada.nome, 'Auxiliar')
        
    def test_listar_funcionarios_por_funcao(self):
        # Criar duas instâncias de "Funcao" para serem associadas aos funcionários
        funcao1 = Funcao.objects.create(nome='Gerente')
        funcao2 = Funcao.objects.create(nome='Analista')

        # Criar três instâncias de "Funcionario", associando cada uma a uma das funções criadas anteriormente
        Funcionario.objects.create(cpf='11111111111', nome='Funcionario 1', funcao=funcao1)
        Funcionario.objects.create(cpf='22222222222', nome='Funcionario 2', funcao=funcao1)
        Funcionario.objects.create(cpf='33333333333', nome='Funcionario 3', funcao=funcao2)

        # Listar os funcionários associados à primeira função criada
        funcionarios_funcao1 = Funcionario.objects.filter(funcao=funcao1)

        # Verificar se a quantidade de funcionários é correta
        self.assertEqual(len(funcionarios_funcao1), 2)

        # Verificar se o nome dos funcionários está correto
        nomes_esperados = {'Funcionario 1', 'Funcionario 2'}
        nomes_obtidos = {funcionario.nome for funcionario in funcionarios_funcao1}
        self.assertEqual(nomes_esperados, nomes_obtidos)

   