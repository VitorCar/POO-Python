# Dunder Methods
# Crie uma classe Produto com atributos nome e preco.
# Implemente __str__ para mostrar nome e preço.
# Implemente __eq__ para comparar produtos pelo nome.

class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        self.__preco = novo_preco

    def __str__(self):
        return f'Produto = {self.nome} -> R${self.__preco:.2f}'      

    def __eq__(self, value):
        return self.nome == value.nome 
    
p1 = Produto('banana', 5.25)
print(p1)

p2 = Produto('kiwi', 8.50)
print(p2)

print(p1 == p2)