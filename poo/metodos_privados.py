class pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.cpf = cpf
        pass

    def apresentar(self):
        print(f'Ola, minha altura - {self.altura}')
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f'Meu documento - {self.cpf}')


vanilda = pessoa('1.55', 'cnisnisi')
vanilda.apresentar()
