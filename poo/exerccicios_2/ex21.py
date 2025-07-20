#Classe com Propriedade e Validação
#Crie uma classe Produto:

#tributos: nome (str), _preco (float).

#Propriedade preco:    @property

#Ao atribuir um valor, só aceita números maiores que 0.

#Se for inválido, lança ValueError.

#Método exibir() que imprime nome e preço formatado.

class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco   # Aqui vai chamar o setter e validar
    
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError('preço não pode ser negativo!')
        self.__preco = valor

    def exibir(self):
        print(f'Nome = {self.nome}\nPreço = R${self.preco:.2f}')

try:
    banana = Produto('Banana', 0)
    banana.exibir()
except ValueError as erro:
    print(f'Erro: {erro}')

#✅ Resumindo:

#O getter e o setter precisam ter o mesmo nome.
#Use atributo privado self.__preco.
#Valide no setter.

