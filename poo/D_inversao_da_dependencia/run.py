# impottar elemento
#A relação que temos aqui e uma dependencia total da classe principal com a class elemento
from elementos.elemento import elemento

class principal:
    def __init__(self):
        self.__elem = elemento() #Ligação direta
        pass

    def run(self) -> None:
        self.__elem.executar()
        print('Estou finalizando na classe principal.')

# a inversao da dependemcia sugere uma relação mais branda
clt = principal()
clt.run()
