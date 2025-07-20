#Classe com método especial __repr__
#Crie uma classe Aluno com atributos nome e matricula.

#Implemente __repr__ para exibir algo como:
#Aluno(nome='João', matricula=12345)

#Crie um objeto e mostre print(repr(objeto)).

class Aluno:
    def __init__(self, nome: str, matricula: int):
        self.nome = nome
        self.matricula = matricula

    def __repr__(self):
        return f'Aluno( Nome = {self.nome} | Matricula = {self.matricula} )'
        
aluno_1 = Aluno('Vanusa', 12345)
print(aluno_1)
print(repr(aluno_1))


#__repr__() tem como objetivo criar uma representação em string que, idealmente, permita reconstruir o objeto original a partir dela. 

#repr() vs. str():
#nquanto __repr__() visa criar uma representação mais técnica e completa, __str__() geralmente foca em uma representação amigável ao usuário. 
