#crie um pequeno sistema:

#Classe base Funcionario com atributos nome e salario.

#Subclasse Gerente que recebe também atributo departamento.

#Método exibir_dados() que imprime todos os dados.

#Crie um objeto Gerente e chame exibir_dados().

class funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.__salario = salario

    def getter_salario(self):
        return self.__salario
    
    def setter_salario(self, salario: float):
        self.__salario = salario

    def exibir(self):
        print(f'Nome = {self.nome}\nSalario = R${self.__salario:.2f}')

    def __str__(self):
        return f'{self.__class__.__name__}: {self.nome}' # Formatando o nome na hora de imprimir colaboradores
        
    
class gerente(funcionario):
    def __init__(self, nome: str, salario: float, departamento: str):
        super().__init__(nome, salario)
        self.departamento = departamento


    def exibir(self):
        super().exibir()
        print(f'Departamento = {self.departamento}')


class estagiario(funcionario):
    def __init__(self, nome: str, salario: float, departamento: str, horas_trabalhadas: int):
        super().__init__(nome, salario)
        self.departamento = departamento
        self.horas = horas_trabalhadas

    def exibir(self):
        super().exibir()
        print(f'Departamento = {self.departamento}\nHoras Trabalhadas = {self.horas} Horas diária')

class diretor(funcionario):
    def __init__(self, nome: str, salario: float, departamento: str, horas_trabalhadas: int, porcentagem_lucro_empresa: int):
        super().__init__(nome, salario)
        #self.__salario = salario
        self.departamento = departamento
        self.horas = horas_trabalhadas
        self.pl = porcentagem_lucro_empresa

    def exibir(self):
        super().exibir()
        base_salario = self.getter_salario()
        soma = base_salario + ( base_salario *  (self.pl / 100)) 
        porcentagem = ( base_salario *  (self.pl / 100)) 
        print(f'Departamento = {self.departamento}\nHoras Trabalhadas = {self.horas} Horas diária')
        print(f'Participação no lucro da empresa = {self.pl}% -> R${porcentagem:.2f}\nReajuste Salario = R${soma:.2f}')     
              



gerente_1 = gerente('Carlos', 6800, 'TI')
#gerente_1.exibir()

estagiario_1 = estagiario('Vitor', 800, 'Analista de Sistemas', 4 )
#estagiario_1.exibir()

diretor_1 = diretor('Joaquin', 1200, 'Diretor Financeiro', 7, 20)
#diretor_1.exibir()

empresa =[gerente_1, estagiario_1, diretor_1]

for colaborador in empresa:
    print(colaborador)
    colaborador.exibir()
    print('-' * 40)




#O que você aprendeu com esse exercício:

#Como herdar uma classe base (Funcionario) e estender com novos atributos (departamento) em Gerente.

#Como usar atributos privados e métodos de acesso (get e set).

#Como usar o super() para reutilizar o método exibir_dados() da classe base.

