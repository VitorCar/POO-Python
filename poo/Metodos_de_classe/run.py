class pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass

    def apresentar(self):
        print(f'Ola meu nome e {self.nome} e tenho {self.idade} anos')

    @classmethod
    def cria_texto(cls, texto):
        nome, idade = texto.split(',')
        return cls(nome, int(idade))
    

pessoa_texto = 'Carlos, 43'
pessoa2 = pessoa.cria_texto(pessoa_texto)
pessoa2.apresentar()