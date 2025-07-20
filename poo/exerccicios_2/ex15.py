#Sobrecarga de operador +
#Crie uma classe Saldo com:

#Um atributo valor.

#Sobrecarga do operador + para somar dois saldos.
#----- Em Python, a sobrecarga de operadores é realizada através da implementação de métodos especiais (conhecidos como métodos "dunder" ou "__" métodos) dentro da classe. Cada operador possui um método correspondente. Por exemplo, para o operador +, o método correspondente é __add__(). Ao definir esse método, você especifica o que acontece quando o operador + é usado com objetos da sua classe. 

class saldo:
    def __init__(self, valor: float):
        self.valor = valor

    def __add__(self, other):
        return saldo(self.valor + other.valor)
    
    def __str__(self):
        return f'saldo = {self.valor}'
    

s1 = saldo(200)
s2 = saldo(400)
s3 = s1 + s2
print(s3)