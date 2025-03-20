class animal:
    def fazer_som(self):
        print('Som generico de animal')

class cachorro(animal):
    def fazer_som(self):
        print('AU au...')

class gato(animal):
    def fazer_som(self):
        print('Miau...')


def fazer_animal_emitir_som(animal):
    animal.fazer_som()


Animal = animal()
dog = cachorro()
cat = gato()

fazer_animal_emitir_som(Animal)
fazer_animal_emitir_som(dog)
fazer_animal_emitir_som(cat)