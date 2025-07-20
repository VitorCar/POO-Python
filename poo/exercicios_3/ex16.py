# Composição
# Crie uma classe Endereco com atributos rua e cidade.
# Crie uma classe Pessoa que contenha um objeto Endereco.
# Implemente método exibir_dados() na Pessoa, exibindo também os dados do endereço.


# Ou seja:

# Herança = Pessoa É um Endereco (não faz sentido aqui)

# Composição = Pessoa TEM um Endereco (é o correto)



class Endereco:
    def __init__(self, rua: str, cidade: str):
        self.rua = rua
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome: str, endereco:Endereco):
        self.nome = nome
        self.endereco = endereco

        
    def exibir_dados(self):
        print(f'Nome = {self.nome}\nRua = {self.endereco.rua}\nCidade = {self.endereco.cidade} ')
        pass

end = Endereco('Nadir', 'juiz de fora')
morador = Pessoa('João', end)
morador.exibir_dados()
        