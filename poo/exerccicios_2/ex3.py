#Crie uma classe Pessoa que tenha:

#Um atributo de classe populacao que conta quantas pessoas foram criadas.

#O construtor deve aumentar esse contador cada vez que um objeto é criado.

#Um método que exibe o nome da pessoa e a população total.

class pessoa:
    populacao = 0  # atributo de class

    def __init__(self) -> None:
        pessoa.populacao += 1
        
    def exibir(self,nome: str) -> None:
        print(f'Ola {nome}\nPopulação = {pessoa.populacao}')

p1 = pessoa()
p1.exibir('Carla')

p2 = pessoa()
p2.exibir('João')