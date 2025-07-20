#Classe com Método de Classe
#Crie uma classe ContaCorrente:

#Atributo de classe taxa_operacao (float).

#Método de classe alterar_taxa(nova_taxa) que altera a taxa.

#Método exibir_taxa() que mostra a taxa atual.

#Teste alterando a taxa e criando objetos.

class ContaCorrente:
    Taxa = 2.6    # atributo de classe

    def __init__(self, titula: str):
        self.titular = titula

    @classmethod
    def alterar(cls, nova_taxa: float):
        cls.Taxa = nova_taxa
        print(f"Taxa alterada para {cls.Taxa}")

    @classmethod
    def exibir(cls):
        print(f"Taxa atual: {cls.Taxa}")


c1 = ContaCorrente('Ana')

# Ver taxa inicial
ContaCorrente.exibir()

ContaCorrente.alterar(3.2)

ContaCorrente.exibir()



        