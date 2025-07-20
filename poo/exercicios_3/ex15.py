# Classe Abstrata e Implementação
# Crie uma classe abstrata Documento com método abstrato validar().
# Implemente CPF e RG como subclasses, cada uma com uma forma fictícia de validação.
# Crie instâncias e chame validar().

from abc import ABC, abstractmethod
from time import sleep

class Documento(ABC):

    @abstractmethod
    def validar(self):
        pass

class CPF(Documento):
    def __init__(self, cpf: str):
        self.cpf = cpf

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf: str):
        self.__cpf = novo_cpf
        if len(str(self.__cpf)) != 8:
            raise ValueError('Deve ter 8 digitos!')
        

    def validar(self):
        print('Validando CPF ...')
        print('-' * 20)
        sleep(1)
        print(f'CPF = {self.__cpf}\nACEITO!')

class RG(Documento):
    def __init__(self, rg: str):
        self.rg = rg
    
    @property
    def rg(self):
        return self.__rg
    
    @rg.setter
    def rg(self, novo_rg: str):
         self.__rg = novo_rg
         if len(str(self.__rg)) != 5:
             raise ValueError('Deve ter 5 digitos!')
       
    def validar(self):
        print('Validando RG ...')
        print('-' * 20)
        sleep(1)
        print(f'RG = {self.__rg}\nACEITO!')

    
        


pessoa1 = CPF(12345678)
pessoa1.validar()
        
pessoa2 = RG(12345)
pessoa2.validar()