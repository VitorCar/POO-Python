#Classe abstrata
#Use o módulo abc:

#Crie uma classe abstrata Forma com método abstrato area().

#Crie duas subclasses: Circulo e Retangulo, que implementam area().

#calcular a área de um círculo, utiliza-se a fórmula: A = π * (r²)  r <- Determine o valor do raio do círculo. 
#retangulo A fórmula geral é: Área = base x altura ou A = b x h. 

#Instancie e calcule as área

from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def area(self):
        pass

class circulo:
    def __init__(self, raio):
        self.raio = raio
        

    def area(self):
        return 3.14 * (self.raio**2)
        

class retangulo:
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento
        

    def area(self):
        return self.largura * self.comprimento
        
    

circulo_1 = circulo(5)
retangulo_1 = retangulo(5, 3)


print(f'A área do circulo = {circulo_1.area()}cm²')
print(f'A área do retangulo = {retangulo_1.area()}cm²')