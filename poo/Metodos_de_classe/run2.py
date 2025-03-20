class pessoa:
    contador = 0 

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pessoa.contador += 1  #INCREMENTA O CONTADOR DA CLASSE
        pass

    def apresentar(self):
        print(f'Ola meu nome e {self.nome} e tenho {self.idade} anos')

    @classmethod
    def contar_pessoa(cls):
        print(f'O total de pessoas criadas: {cls.contador}')


pessoa1 = pessoa('Ana', 21)
pessoa2 = pessoa('Pedro', 54)
pessoa.contar_pessoa()
pessoa1.apresentar()