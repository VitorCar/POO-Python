#QUEBRA DO PRINCIPIO DE LISKOV
class animal:
    def alimentar(self):
        print('O animal esta se alimentando.')

class cachorro(animal):
    def latir(self):
        print('O cachorro esta latindo')

class peixe(cachorro):
    def nadar(self):
        print('O peixe esta nadando')

    def latir(self):  #comportamento diferente entre class pai e class filha
        raise Exception('Peixe nao late') # comportamento de levantar um erro 
# raise exception : e uma forma controlada de interronper o fluxo normal,
#de um codigo e tomar as medidas apropriadas com base no erro.
    
def Verificar_animal(animal: any):
    animal.latir()

obj1 = animal()
obj2 = cachorro()
obj3 = peixe()
Verificar_animal(obj2)