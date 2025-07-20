#Crie uma classe ContaBancaria com:

#Um atributo saldo inicializado com 0.

#Um método depositar(valor) que aumenta o saldo.

#Um método sacar(valor) que diminui o saldo.

#Um método mostrar_saldo() que imprime o saldo atual.

#Faça depósitos e saques e exiba o saldo final.

class contabancaria:
    def __init__(self) -> None:
        self.valor = 0
        
    def depositar(self, valor: float) -> None:
        self.valor = valor
        print(f'Você depositou R${valor:.2f}')

    def sacar(self, sac: float) -> None:
        diminuir = self.valor - sac
        if sac > self.valor:
            print(f'VocÊ não tem R${sac:.2f} em conta!')
        else:
            print(f'Saque = R${sac:.2f}\nSaldo = R${diminuir:.2f}')

cliente = contabancaria()
cliente.depositar(200)
cliente.sacar(100)