from abc import ABC, abstractmethod

class trabalhador(ABC):  #INTERFACE

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self):
        pass

    @abstractmethod
    def consultar_beneficio(self):
        pass
# A ideia em si estabelece que uma classe não deve ser forçada a depender
# uma interface que ela não utiliza 

class trabalhador_Temporario(ABC):  #INTERFACE criada para o prof substituto

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self):
        pass

class professor(trabalhador):  #implementaçao de uma classe
    def trabalhar(self):
        print('O prof esta trabalhando.')

    def ir_para_casa(self):
        print('O profe esta indo para casa.')

    def consultar_beneficio(self):
        print('Consultando beneficios...')

class professorSubstitudo(trabalhador_Temporario): 
    def trabalhar(self):
        print('O prof substituto esta trabalhando.')

    def ir_para_casa(self):
        print('O profe substituto esta indo para casa.')
        

    
p2= professorSubstitudo()
