#Abstração
#Crie uma classe abstrata UsuarioBase com:

#método abstrato exibir_informacoes()

#atributo email

#Depois, crie uma classe concreta Cliente que:

#herde de UsuarioBase

#tenha atributos nome e telefone

#implemente o método exibir_informacoes(), mostrando todos os dados
from abc import ABC, abstractmethod

class UsuarioBase(ABC):
    def __init__(self, email: str):
        self.email = email

    @abstractmethod
    def exibir_informações(self):
        print(f'Email = {self.email}')

class Cliente(UsuarioBase):
    def __init__(self, email, nome: str, telefone: int):
        super().__init__(email)
        self.nome = nome
        self.telefone = telefone

    def exibir_informações(self):
        print(f'Nome = {self.nome}\nTelefone = {self.telefone}')
        super().exibir_informações()

cliente_1 = Cliente('carlos@gmai.com', 'Carlos Henrique', 123456789)
cliente_1.exibir_informações()