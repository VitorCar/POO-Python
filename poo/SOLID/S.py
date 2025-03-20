class Sistemacadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validar_input(nome, idade):
            self.__registrar(nome, idade)
        else:
            self.__error()
        


    def __validar_input(self, nome: str, idade: int) -> bool:  # 1
        return isinstance (nome, str) and isinstance(idade, int)
    

    def __registrar(self, nome: str, idade: int) -> None:   # 2
        print('Acessando o banco de dados...')
        print(f'Cadastrar o usario {nome}, idade {idade}')


    def __error(self) -> None:    # 3
        print('Dados invalidos')



pessoa = Sistemacadastral()
pessoa.cadastrar('carina', 44)
# SE COLOCAR IDADE COMO STR VAI DAR O COMANDO ERROR  ex :'44a'
