#Classe com Composição
#Crie uma classe Endereco:

#Atributos: rua, numero, cidade.

#E uma classe Cliente:

#Atributos: nome e endereco (objeto Endereco).

#Método exibir() que imprime nome e endereço completo.

class Endereco:
    def __init__(self, rua: str, numero: int, cidade: str):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        
    def exibir(self):
        print(f'Rua = {self.rua}\nNúmero = {self.numero}\nCidade = {self.cidade}')

class Cliente:
    def __init__(self, nome: str, endereco: Endereco):    # Composição
        self.nome = nome
        self.endereco = endereco    # Composição
        
    def exibir(self):
        print(f'Nome = {self.nome}')
        self.endereco.exibir()   # Chama o método que imprime o endereço

casa_1 = Endereco('Nadir Mendonça', 44, 'Santos')
#criamos o cliente, passando o objeto endereco
morador = Cliente('Carlos', casa_1)
morador.exibir()