class conectarbancodedados:
    def __init__(self) -> None:
        self.conectar = None
        pass

    def conectar_ao_banco(self) -> None:
        self.conectar = True

class RepositoriodeBanco:
    def __init__(self, conexao: conectarbancodedados) -> None:
        self.__conexao = conexao
        pass

    def busc_dados(self) -> list:
        if self.__conexao.conectar:
            return [1, 2, 4, 6, 8]
        return None
    
class RegradeNegocio:
    def __init__(self, repo: RepositoriodeBanco) -> None:
        self.__repo = repo
        pass

    def calcular_resutado(self) -> None:
        dados = self.__repo.busc_dados()
        if not dados:
            print('Dados não encontrados. Verifique sua conexão com o banco')
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f'o resutado e: {resposta}')

conn = conectarbancodedados() #ESTOU CONECTANDO AO BANCO
conn.conectar_ao_banco()

repo = RepositoriodeBanco(conn)  #COLOCANDO O BANCO NO REPOSITORIO
regra = RegradeNegocio(repo)  #COLOCANDO O REPOSITORIO DENTRO DA REGRADENEGOSIO
# E UM EXEMLPO BEM FEITO POIS UM REALMENTE NECESSITA DA EXISTENCIA DO OUTRO
regra.calcular_resutado()
