 #Polimorfismo
#Crie uma lista com objetos de diferentes classes:

#Gato e Cachorro, ambos com método falar().

#Faça um loop que percorre a lista e chama falar() de cada objeto.

class animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f'{self.nome} faz um som...')

class cachorro(animal):
    def falar(self):
        print(f'O {self.nome} late.')

class gato(animal):
    def falar(self):
        print(f'O gato {self.nome} mia.')

# criando uma lista com obj diferentes

animais = [cachorro('Ragner'), gato('Tom'), animal('Humano')]

# loop polimorfico
for animal in animais:
    animal.falar()
