#Herança + Polimorfismo
#Crie uma classe Funcionario com método calcular_salario(), que retorna 0.

#Crie duas subclasses:

#FuncionarioCLT: retorna salário fixo de R$2000

#FuncionarioPJ: retorna salário fixo de R$4000

#Crie uma lista com objetos de ambas as classes e imprima os salários usando polimorfismo.

class Funcionario:
    def calcular_salario(self):
        pass

class FuncionarioCLT(Funcionario):
    def calcular_salario(self):
        print('salário fixo de R$2000')
    
class FuncionarioPJ(Funcionario):
    def calcular_salario(self):
        print('salário fixo de R$4000')

f1 = FuncionarioCLT()
f2 = FuncionarioPJ()
f3 = FuncionarioCLT()
f4 = FuncionarioPJ()

lista_funcionario = [f1, f2, f3, f4]
for f in lista_funcionario:
    f.calcular_salario()