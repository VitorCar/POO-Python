#Sobrecarga do operador de igualdade ==
#Crie uma classe Pessoa com:

#Atributos nome e idade.

#Sobrecarga de __eq__ para retornar True se nome e idade forem iguais.

#Teste comparando duas pessoas.

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade 

    def __eq__(self, other):
        return self.nome == other.nome and self.idade == other.idade
        
    def __str__(self):
        return f'{self.nome}, {self.idade} anos'
    

p1 = Pessoa('joao', 22)
p2 = Pessoa('joao', 22)
p3 = Pessoa('maria', 20)
#O == só usa o resultado booleano retornado pelo __eq__.
print(p1 == p2) #True
print(p1 == p3) #False

#O __str__ só aparece quando você faz:
print(p1)