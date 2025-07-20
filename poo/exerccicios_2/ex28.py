#Classe com Sobrecarga de __repr__
#Crie uma classe Pedido:

#Atributos: id_pedido (int), valor (float).

#Método __repr__ que retorna

class Pedido:
    def __init__(self, id_pedido: int, valor: float):
        self.__id_pedido = id_pedido
        self.valor = valor

    @property
    def id_pedido(self):
        return self.__id_pedido
    
    @id_pedido.setter
    def id_pedido(self, novo_id: int):
        self.__id_pedido = novo_id

    def __repr__(self):
        return f'id = {self.__id_pedido} | Valor =  R${self.valor:.2f}'
        
    def __str__(self):
        return f'{self.__id_pedido}\n{self.valor:.2f}'


p1 = Pedido(2,250)
print(repr(p1))
print(p1)    

#Quando usar __repr__ e __str__?
#__repr__: Usado para fornecer uma representação inequívoca de um objeto, ideal para depuração e desenvolvimento. Se __str__ não estiver definido, __repr__ também será usado pela função print().
#__str__: Usado para fornecer uma representação mais amigável do objeto para o usuário final. Se __str__ não estiver definido, __repr__ será usado pela função print(). 


#🧠 Resumo em 1 frase:
#Use __repr__ para dar uma representação clara e completa que sirva ao programador, e __str__ para uma forma bonitinha e amigável para quem vai ver a saída.
