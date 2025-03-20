class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass

    def apresentar(self):
        print(f'Ola, meu nome e {self.nome} e tenho {self.idade} anos')
    
pessoa1 = Pessoa('victoria', 32)
pessoa2 = Pessoa('analice', 41)

pessoa1.apresentar()
pessoa2.apresentar()