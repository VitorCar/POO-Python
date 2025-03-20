from abc import ABC, abstractmethod

class trabalhador(ABC):  #INTERFACE

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self):
        pass

    @abstractmethod
    def horario_de_ir(self):
        pass

class professor(trabalhador):  #implementaçao de uma classe
    def trabalhar(self):
        print('O prof esta trabalhando.')

    def ir_para_casa(self):
        print('O profe esta indo para casa.')

    def horario_de_ir(self):
        print('O professor foi...')

def comunicar_trabalhador(trabalhador: trabalhador):
    trabalhador.trabalhar()
    print('Comunicar o trabalhador para ir para casa.')
    trabalhador.ir_para_casa()

p1 = professor()
comunicar_trabalhador(p1)