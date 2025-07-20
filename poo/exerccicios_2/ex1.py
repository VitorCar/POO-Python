#Crie uma classe chamada Carro com:

#Um atributo marca e um atributo ano.

#Um método que exibe esses dados formatados.

#Crie dois objetos com marcas e anos diferentes e chame o método de exibição.


class carro:
    def __init__(self, marca: str, ano: int) -> None:
        self.marca = marca
        self.ano = ano
        pass

    def exibir(self) -> None:
        print(f'O seu carro e da marca = {self.marca}\nAno = {self.ano}')

Uno = carro('Fiat', 2004)
Uno.exibir()

