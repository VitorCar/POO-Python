#Classe com método de classe
#Crie uma classe Produto que tenha:

#Atributos nome e preco.

#Um atributo de classe imposto com valor inicial 0.1 (10%). @classmethod

#Um método de classe que altera o imposto.         @classmethod

#Um método que calcula o preço final com imposto.    @classmethod

#Demonstre alterando o imposto.

class produto:
    imposto = 10

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def consultar_produto(self):
        porcentagem = self.preco * self.imposto / 100
        novo_preco = self.preco + porcentagem
        print(f'Nome = {self.nome}\nPreço = R${self.preco}\nTaxa imposto = {self.imposto}% -> R${porcentagem:.2f}')
        print(f'Preço com Imposto = R${novo_preco:.2f} ')

    @classmethod
    def alterar_imposto(cls, imposto: float):
        cls.imposto = imposto        


caneta = produto('Caneta', 100)
caneta.consultar_produto()

print('\n----------- Novo Imposto --------')
caneta.alterar_imposto(40)
caneta.consultar_produto()

        