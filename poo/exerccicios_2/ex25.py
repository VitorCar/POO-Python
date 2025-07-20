#Classe com Sobrecarga de __contains__
#Crie uma classe Biblioteca:

#Atributo livros (lista de strings).

#Sobrecarga de __contains__   É um método especial do Python que permite usar o operador in com seu objeto.

class Biblioteca:
    def __init__(self, livros):
        self.livros = livros
        
    def __contains__(self, item):
        # Retorna True se 'item' estiver na lista de livros
        return item in self.livros
    
romance = Biblioteca(['Lua', 'Sol', 'Amanhecer'])
print('Lua' in romance)
print('oi' in romance)

#🧠 Resumo do que você aprendeu
#__contains__ é o método que habilita in.

#Recebe o elemento procurado como item.

#Retorna True ou False.

#Assim, seu objeto se comporta como uma lista para verificação de existência.

