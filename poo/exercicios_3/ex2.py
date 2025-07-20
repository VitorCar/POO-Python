# Encapsulamento
#Crie uma classe Produto com:

#atributo privado __preco

#atributo nome

#propriedade preco com getter e setter

#o setter deve impedir valores <= 0

#método exibir()

class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco    # Chama o setter aqui

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco <= 0:
            raise ValueError("O preço deve ser maior que zero!")
        self.__preco = novo_preco
        

    def exibir(self):
        print(f'Produto = {self.nome}\nPreço = R${self.__preco:.2f}')

produto_1 = Produto('Caneta', 45)
produto_1.exibir()