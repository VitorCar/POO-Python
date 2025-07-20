 #Herança com Construtores
#Crie:

#Uma classe Veiculo com atributos marca e modelo.

#Uma subclasse Moto que adiciona o atributo cilindradas.

#Lembre-se de chamar o construtor da classe pai usando super().

#Crie um objeto Moto e exiba todos os atributos.

class veiculo:
    def __init__(self, marca: str, ano: int) -> None:
        self.marca = marca
        self.ano = ano
        

class carro(veiculo):
    def __init__(self, marca, ano, cavalos: int):
        super().__init__(marca, ano)
        self.cavalos = cavalos

    def exibir(self) -> None:
        print(f'Marca = {self.marca}\nAno = {self.ano}\nCavalos = {self.cavalos}')


class moto(veiculo):
    def __init__(self, marca, ano, cilindradas: int):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def exibir(self) -> None:
        print(f'Marca = {self.marca}\nAno = {self.ano}\nCavalos = {self.cilindradas}')




uno = carro('Fiat', 2008, 68)
uno.exibir()

bis = moto('Honda', 2018, 120)
bis.exibir()