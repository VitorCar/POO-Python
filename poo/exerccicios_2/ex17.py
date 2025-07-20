 #Polimorfismo com lista de objetos
#Crie:

#Uma classe base Funcionario com método calcular_pagamento().

#Subclasses Mensalista e Horista com cálculos diferentes.

#Crie uma lista com objetos de ambas e mostre os pagamentos no loop.

class Funcionario:
    preco_dia = 60
    preco_hora = 7.5

    def __init__(self, nome):
        self.nome = nome

    def calcular_pagamento(self):
        pass

class Mensalista(Funcionario):
    def __init__(self, nome, dias_mes: int):
        super().__init__(nome)
        self.dias_mes = dias_mes

    def calcular_pagamento(self):
        calculo = self.dias_mes * self.preco_dia
        print(f'Nome = {self.nome}\nDias trabalhdos no mÊs = {self.dias_mes}\nSalario = R${calculo:.2f}')

class Horista(Funcionario):
    def __init__(self, nome, horas_dia: float):
        super().__init__(nome)
        self.horas_dia = horas_dia


    def calcular_pagamento(self):
        calculo = self.horas_dia * self.preco_hora
        print(f'Nome = {self.nome}\nHoras trabalhadas no dia = {self.horas_dia} Horas\nSalario do dia = R${calculo:.2f}')


funcionario_1 = Mensalista('Andre', 20)
funcionario_2 = Horista('Carla', 6)
funcionario_3 = Mensalista('Tarzan', 18)
funcionario_4 = Horista('João', 8)

pagamentos = [funcionario_1, funcionario_2, funcionario_3, funcionario_4]

for pg in pagamentos:
    pg.calcular_pagamento()
    print('-' * 50)

