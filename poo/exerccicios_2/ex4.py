#Encapsulamento com Atributos Privados

#Crie uma classe Funcionario com:

#Um atributo privado _salario.

#Métodos set_salario(valor) e get_salario() para alterar e consultar o salário.

#Um método exibir_informacoes() que mostra o nome e o salário.

#Crie um objeto e teste os métodos.

class funcionario:
    def __init__(self) -> None:
        self__salario = None
        

    def setter_salario(self, valor: float) -> None:
        funcionario.__salario = valor

    def getter_salario(self) -> float:
        return funcionario.__salario
    
    def exibir(self):
        valor = funcionario.__salario
        print(f'Salario = R${valor:.2f}')

vitor = funcionario()
vitor.setter_salario(2400)
print(vitor.getter_salario())
vitor.exibir()
