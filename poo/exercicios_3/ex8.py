#Abstração + Encapsulamento
#Crie uma classe abstrata NotificacaoBase com:

#método abstrato enviar(mensagem)

#Crie as subclasses:

#NotificacaoEmail: enviar() imprime "Email enviado: {mensagem}"

#NotificacaoSMS: enviar() imprime "SMS enviado: {mensagem}"
from abc import ABC, abstractmethod

class NotificacaoBase(ABC):

    @abstractmethod
    def enviar(self, mensagem: str):
        pass

class NotificacaoEmail(NotificacaoBase):
    def enviar(self, mensagem: str):
        print(f'Email Enviado!\nMensagem = {mensagem}')

class NotificacaoSMS(NotificacaoBase):
    def enviar(self, mensagem: str):
        print(f'SMS Enviado!\nMensagem = {mensagem}')


mensagem_1 = NotificacaoEmail()
mensagem_1.enviar('Ola, mundo!')

mensagem_2 = NotificacaoSMS()
mensagem_2.enviar('Boa Noite!')