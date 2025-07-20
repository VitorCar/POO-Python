#Crie uma classe Retangulo:

#Atributos largura e altura.

#Uma propriedade area que calcula largura * altura.

#Crie um objeto e mostre a área.

class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    #O decorador @property transforma um método em um atributo calculado.
    @property
    def area(self):
        return self.largura * self.altura
        


ret = retangulo(8, 6)
print(f'Area = {ret.area}')

#Usando @property, você deixa seu código:

#Mais elegante

#Com interface mais natural (ret.area em vez de ret.area())

