from abc import ABC, abstractmethod  # sao os elementos abstratos que temos em python
#ABC maiusculo que e uma classe , e chamda de criadora de class abstratas 
# abstractmethod > metodo abstrato 
class pessoa(ABC):  # a class pessoa se torna uma class abstrata
    def correr(self):    # classes abstratas nao possui objetos > so pode ser mae(Herança)
        print('A pessoa esta correndo de manha.')

 # criando o metodo abstrato
    @abstractmethod # classe filha DEVE criar um metodo trabalhar
    def trabalhar(self):
        pass

class professor(pessoa):
    def trabalhar(self):
       print('O professor esta dando aula')


class cozinheiro(pessoa):
    def trabalhar(self):
        print('O cozinheiro esta cozinhado...')


p1 = professor()
p1.trabalhar()
p1.correr()
