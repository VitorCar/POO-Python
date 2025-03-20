class classequalquer:
    def fazer(self) -> None:
        print('Estou fazendo algo')


class Outracoisa(classequalquer):
    def preparar(self) -> None:
        print('Estou preparando algo')

    def fazer(self):  #ESTA SOBREESCREVENDO O METODO DE CIMA 
        print('Estou fazendo outra coisa.')

obj1 = classequalquer()
obj2 = Outracoisa()

obj1.fazer()
obj2.fazer()  # VAI SOBRE ESCREVER 
