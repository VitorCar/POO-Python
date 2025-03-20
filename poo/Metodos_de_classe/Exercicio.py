class loja:
    taxa = 1.20
    

    def __init__(self, valor: float):
        self.valor_produto_bruto = valor
        pass

    def consultar_valor_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f'Valor do produto: {valor_produto}')

    @classmethod
    def editar_taxa_do_produto(cls, valor: float):
        cls.taxa = valor 


loja_cabo_frio = loja(40.25)
loja_rj = loja(35.15)
loja_sp = loja(20.10)

loja_cabo_frio.consultar_valor_produto()
loja_rj.consultar_valor_produto()
loja_sp.consultar_valor_produto()

#ALTERANDO TAXA
print('-------TAXA EDITADA---------')
loja_cabo_frio.editar_taxa_do_produto(1.45)

loja_cabo_frio.consultar_valor_produto()
loja_rj.consultar_valor_produto()
loja_sp.consultar_valor_produto()