#Classe Abstrata com Método Abstrato
#Crie uma classe abstrata Veiculo com método abstrato mover().

#Crie subclasses Carro e Bicicleta que implementem mover():

#Carro imprime "Dirigindo o carro".

#Bicicleta imprime "Pedalando a bicicleta".

from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print('Dirigindo o carro!')


class Bicicleta(Veiculo):
    def mover(self):
        print('Pedalando a bicicleta!')

carro_1 = Carro()
carro_1.mover()

bike = Bicicleta()
bike.mover()