# Propriedades e Exceções
# Crie uma classe Temperatura com propriedade celsius.
# Ao tentar definir um valor abaixo de -273, levante ValueError.
# Implemente um método que retorne a temperatura em Fahrenheit.   A fórmula é: °F = (°C × 1.8) + 32 ou °F = (°C × 9/5) + 32. 

class Temperatura:
    def __init__(self, celsius: int):
        if celsius < -273:
            raise ValueError('Valor muito baixo!')
        self.celsius = celsius

    def calcular(self):
        return(self.celsius * 1.8) + 32
    
    def exibir(self):
        fahrenheit = self.calcular()
        print(f'Celsius = {self.celsius}\nFahrenheit = {fahrenheit}')
 

calor = Temperatura(25)
calor.exibir()