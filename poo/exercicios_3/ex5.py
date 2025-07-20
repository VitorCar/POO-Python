#Abstração + Herança
#Crie uma classe abstrata PagamentoBase com:

#método abstrato processar()

#atributo valor

#Crie as subclasses:

#PagamentoCartao

#processar() imprime "Processando pagamento com cartão no valor de R$X"

#PagamentoBoleto

#processar() imprime "Gerando boleto no valor de R$X"

from abc import ABC, abstractmethod

class PagamentoBase(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def processar(self):   #um método abstrato não deve ter corpo (ou no máximo pass).
        pass
        
class PagamentoCartao(PagamentoBase):
    def processar(self):
        
        print(f"Processando pagamento com cartão no valor de R${self.valor}")

class PagamentoBoleto(PagamentoBase):
    def processar(self):
        
        print(f"Gerando boleto no valor de R${self.valor:.2f}")



p1 = PagamentoCartao(2400)
p1.processar()


#O decorador @abstractmethod serve para dizer:

#"Esta função NÃO TEM implementação e deve ser obrigatoriamente implementada pelas subclasses".
