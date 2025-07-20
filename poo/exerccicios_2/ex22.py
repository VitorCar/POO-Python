 #Classe com Método Estático de Utilidade
#Crie uma classe Matematica:

#Método estático fatorial(n) que calcula o fatorial de n.      @staticmethod

#Método estático potencia(base, expoente) que calcula base ^ expoente.      @staticmethod

#Teste os métodos sem instanciar a classe.

class Matematica:
    @staticmethod
    def fatorial(n: int):
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial
    
    def potencia(base, expoente):
        return base ** expoente
    

fat = Matematica.fatorial(4)
print(f'4! = {fat}')

pot = Matematica.potencia(2,3)
print(f'potencia 2³ = {pot}')