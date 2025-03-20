class Interruptor:
    def __init__(self, comodo: str)-> None:
        self.comodo = comodo
        pass

    def acende(self):
        print(f'Estou acendendo a luz do comodo: {self.comodo}')

    def apagar(self):
        print(f'Estou apagando a luz do comodo: {self.comodo}')


class pessoa:
    def acender_luz(self, interruptor: Interruptor): #juntando as duas classes
        interruptor.acende()

    def apagar_luz(self, interruptor: Interruptor): #RELACIONAMENTO DE CLASSES
        interruptor.apagar()

    def dormir(self):
        print('A pessoa foi dormir.')

raimundo = pessoa()
interruptor_sala = Interruptor('sala')
interruptor_banheiro = Interruptor('banheiro')

raimundo.acender_luz(interruptor_sala)
raimundo.apagar_luz(interruptor_banheiro)
