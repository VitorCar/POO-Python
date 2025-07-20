#  Encapsulamento com Validação
# Crie uma classe ContaCorrente com atributo privado __saldo.
# Implemente métodos depositar(valor) e sacar(valor).
# O método sacar deve levantar ValueError se o saldo for insuficiente.

class ContaCorrente:
    def __init__(self, saldo: float):
        self.saldo = saldo 

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo:float):
        if novo_saldo < 0 :
            raise ValueError('O saldo inicial não pode ser negativo!')
        self.__saldo = novo_saldo
    
    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O deposito deve ser positivo.')
        self.__saldo += valor
        print(f'Deposito R${valor:.2f}')
        
    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O saque deve ser positivo")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= valor
        print(f"Sacado R${valor:.2f}")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")


conta_1 = ContaCorrente(2400)
conta_1.exibir_saldo()
conta_1.depositar(200)
conta_1.exibir_saldo()
conta_1.sacar(3000)