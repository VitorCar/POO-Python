 #Classe com propriedade de leitura e escrita
#Crie uma classe Quadrado com:

#Um atributo lado.

#Uma propriedade area que calcula lado * lado.   @property

#Uma propriedade perimetro que calcula 4 * lado.   @property

#Crie um objeto e mostre a área e o perímetro.

class quadrado:
    def __init__(self, lados: int):
        self.lados = lados
        
    @property
    def calcular_lados(self):
        return self.lados * self.lados
       
    @property
    def perimetro(self):
        return 4 * self.lados
        

q = quadrado(8)
print(f'ÁREA = {q.calcular_lados}')
print(f'PERIMETRO = {q.perimetro}')

# é fundamental usar @property e retornar os valores ao invés de imprimir direto dentro do método.