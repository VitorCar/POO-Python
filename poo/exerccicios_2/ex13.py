#Classe com método estático
#Crie uma classe ConversorTemperatura com:

#Um método estático celsius_para_fahrenheit(celsius).   A fórmula é: °F = (°C × 1.8) + 32 ou °F = (°C × 9/5) + 32. 

#Um método estático fahrenheit_para_celsius(fahrenheit).   Fahrenheit para Celsius, a fórmula é: C = (F - 32) / 1.8

#Teste os métodos sem instanciar a classe.    @staticmethod

class ConversorTemperatura:
    @staticmethod
    def celsius_para_fahrenheit(Celsius: float):
        return (Celsius * 1.8) + 32

    def fahrenheit_para_celsius(fahrenheit: float):
        return (fahrenheit - 32) / 1.8

        


c_para_f = ConversorTemperatura.celsius_para_fahrenheit(25)
print(f'Resultado celsius para fahrenheit = {c_para_f}')

f_para_c = ConversorTemperatura.fahrenheit_para_celsius(77)
print(f'O resultado fahrenheit para celsius = {f_para_c}')


#Decoração:
#O decorador @staticmethod é aplicado a um método dentro de uma classe. Isso informa ao Python que esse método não deve receber self ou cls como primeiro argumento. 

#Sem acesso à instância/classe:
#Métodos estáticos não têm acesso direto aos atributos da instância (variáveis definidas com self) ou aos atributos da classe (variáveis definidas na própria classe). 