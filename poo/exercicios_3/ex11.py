# Herança e Métodos da Superclasse
# Crie uma classe Veiculo com atributos marca e ano, e método exibir_dados().
# Crie uma subclasse Moto que herde de Veiculo e tenha um atributo cilindrada.
# Implemente exibir_dados() na Moto chamando o método da superclasse e exibindo também a cilindrada.

class Veiculo:
    def __init__(self, marca: str, ano: int):
        self.marca = marca
        self.ano = ano

    def exibir(self):
        print(f'Marca = {self.marca}\nAno = {self.ano}')

class Moto(Veiculo):
    def __init__(self, marca: str, ano: int, cilindrada: int):
        super().__init__(marca, ano)
        self.cilindrada = cilindrada

    def exibir_dados(self):
        self.exibir()
        print(f'Cilindradas = {self.cilindrada}')


moto_1 = Moto('Yamaha', 2022, 244)
moto_1.exibir_dados()