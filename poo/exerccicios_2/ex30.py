#Classe com Propriedade Calculada
#Crie uma classe Retangulo:

#Atributos: largura e altura.

#Propriedade area que calcula largura * altura.

#Propriedade perimetro que calcula 2*(largura + altura).

#Crie um objeto e imprima área e perímetro.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura
    
    @property
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
    def __str__ (self):
        return f'{self.largura} X {self.altura} = {self.area}\nPerimetro = {self.perimetro}'
    
    def __repr__(self):
        return f'Retangulo(largura={self.largura}, altura={self.altura})'

        

r1 = Retangulo(4, 4)
print(r1)
print(repr(r1))


#🧠 Resumindo:
#Quando você chama:

#print(r1) → usa __str__()

#repr(r1) ou só digitar r1 no console → usa __repr__()

#str(r1) → usa __str__()

#💡 Dica
#Se você não definir __str__, o print() cai automaticamente no __repr__.
#Então sempre que quiser um formato “bonitinho”, crie o __str__.
#Quando quiser um formato técnico (debug), crie o __repr__.

