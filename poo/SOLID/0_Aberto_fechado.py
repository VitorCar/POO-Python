#ESTA NO PRINCIPIO ABERTO/FECHADO
class artista:
    def __init__(self, tipo: str):   #o tipo de artista
        self.tipo = tipo
        pass

    def apresentar_show(self) -> None:   #none nao retorna nada
        print(f'O {self.tipo} esta apresentando seu show')


class circo:    # a clase que nao se altero
    def apresentar(self, artista: artista) -> None:   #O artista vai receber a classe artista
        print('O circo esta abrindo!')
        artista.apresentar_show()
        print('O publico aplaude!')


Circo = circo()       

palhaco = artista('palhaco')
magico = artista('magico')
malabarista = artista('malabarista')

Circo.apresentar(magico)