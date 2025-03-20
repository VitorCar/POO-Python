# criar uma class animal
class animal:
    def __init__(self, nome: str, especie: str, idade: int):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        pass

    def emitir_som(self):
        print('Som de animal...')

    def apresentar(self):
        print(f'nome: {self.nome} - especie: {self.especie} - idade: {self.idade}')

class cachoro(animal):
    def __init__(self, nome, especie, idade):
        super().__init__(nome, especie, idade)
        self.emitir_som() 
        print('AU, AU!')
        self.apresentar()

class gato(animal):
    def __init__(self, nome, especie, idade):
        super().__init__(nome, especie, idade)
        self.emitir_som()
        print('MIAUU!')
        self.apresentar()




zoe = cachoro('zoe', 'canina', 3)
zoe.emitir_som
zoe.apresentar
print('-' * 55)
fred = gato('fred', 'felino', 2)
zoe.emitir_som
zoe.apresentar