#relação para que o elemento e a função principal fique mais branda
from elementos.interfaces.elemento_interface import elementoInterface
from elementos.elemento import elemento

class principal:
    def __init__(self, elem: elementoInterface)-> None:
        self.__elem = elem
        pass

    def run(self) -> None:
        self.__elem.executar()
        print('Estou finalizando na classe principal.')

#Nao tem mais uma dependencia forte da classe principal
el = elemento()
cl1 = principal(el)
cl1.run()