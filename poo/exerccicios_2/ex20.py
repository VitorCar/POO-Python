#Classe com propriedade que valida valor
#Crie uma classe ContaBancaria com:

#tributo privado __saldo.

#Uma propriedade saldo que só aceita valores >= 0.

#Se tentar setar saldo negativo, lance um ValueError

# use propriedades para controlar o acesso ao saldo.

#Teste a validação.

class ContaBancaria:
    def __init__(self, saldo: int):
        self.saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError('Saldo não pode ser negativo.')
        self.__saldo = valor
   
    def exibir(self):
        print(f"Saldo = R${self.__saldo:.2f}")


try:
    conta1 = ContaBancaria(500)
    conta1.exibir()
    conta1.saldo = 200
    conta1.exibir()
    conta1.saldo = -50  # Vai lançar ValueError aqui
except ValueError as e:
    print(f"Erro: {e}")

#Resumo da lógica:
#1️⃣ Use @property para criar um getter do saldo.
#2️⃣ Use @saldo.setter para criar um setter que valida se é >= 0.
#3️⃣ No construtor, use self.saldo = saldo (assim ele já passa pelo setter).
#4️⃣ Lançe ValueError se for inválido.
#5️⃣ No programa principal, use try...except para capturar o erro.

