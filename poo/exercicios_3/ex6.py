 #Encapsulamento + Propriedades
#Crie uma classe Pedido com:

#atributo privado __status

#propriedade status com getter e setter

#o setter só aceita "aberto", "pago", "cancelado"

#método exibir()

class Pedido:
    def __init__(self, status: str):
        self.status = status

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, novo_status: str):
        if novo_status not in ('aberto','pago','cancelado'):
            raise ValueError('Só aceitamos: aberto, pago, cancelado')
        self.__status = novo_status

    def exibir(self):
        print(f'Status = {self.__status}')

pedido1 = Pedido('aberto')
pedido1.exibir()