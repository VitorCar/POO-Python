  #Métodos Especiais
#Crie uma classe Produto:

#Atributos nome e preco.

#Implemente __str__ para exibir uma string formatada: “Produto: [nome], Preço: [preco]”.

#Crie um objeto e imprima ele diretamente (print(objeto)).

class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'Produto: {self.nome}\nPreço: {self.preco}'

p = produto('Mouse', 85)
print(p) #executando deu: <__main__.produto object at 0x0000026771BA7380>

#O __str__ deve retornar uma string com a apresentação que você quiser:

#__str__ é chamado quando:

#Você faz print(objeto)

#Ou str(objeto)

#Retorna uma string representando o objeto.

