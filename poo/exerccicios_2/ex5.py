#Herança Simples

#Crie duas classes:

#Animal: com método falar() que imprime “O animal faz um som.”

#Cachorro: que herda de Animal e sobrescreve falar() para imprimir “O cachorro late.”

#Crie um objeto Cachorro e chame falar().

class animal:
    def __init__(self) -> None:
        pass

    def falar(self) -> None:
        print('O animal faz um som...')


class cachorro(animal):
    def __init__(self):
        super().__init__()

    def falar(self):
        print('O cachorro late!')

dog = cachorro()
dog.falar()