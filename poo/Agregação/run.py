class produto:
    def __init__(self, nome: str, valor: int) -> None:
        self.__nome = nome
        self.__valor = valor
        pass

    def informaçoes_do_produto(self) -> None:
        print(f'Produto: {self.__nome} - valor: {self.__valor}')


class carrinhodecompra:
    def __init__(self) -> None:
        self.__produtos = []
        pass

    def adicionar_produto(self, produto: produto) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        print('Compra Finalizada!')
        print('   PRODUTOS:   ')
        for prod in self.__produtos:
            prod.informaçoes_do_produto()
            
#Objetos que sao carregados por outros objetos

banana = produto('Banana', 5)
uva = produto('Uva', 8)
pera = produto('Pera', 3)

carrinho = carrinhodecompra()
carrinho.adicionar_produto(banana)
carrinho.adicionar_produto(uva)
carrinho.adicionar_produto(pera)

carrinho.finalizar_compra()