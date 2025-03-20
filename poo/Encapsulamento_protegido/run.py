class Mamifero:
    def __init__(self, localizacao: str):
        self.localizacao = localizacao
        self. _tamanho = '1.22'
        pass

    def andar(self) -> None:
        print(f'O animal esta andando pelo: {self.localizacao}')

    def _dormir(self) -> None:  #METODO PROTEGIDO
        print('O animal esta dormindo!')
#ACESSIVEL DENTRO DA PROPRIA CLASS / MAS QUE POSSA SER ACESSADO POR OUTRAS 
#CLASS FILHAS
class gato(Mamifero):
    def __init__(self, localizacao: str):
        super().__init__(localizacao)

    def miar(self) -> None:
        print('O gato esta miando')
        self._dormir()
        print(self._tamanho)

cat = gato('Uberlandia')
cat.miar()
cat._dormir() #DEVERIA DAR ERROR/ ELEMENTOS PROTEGIDOS NAO SAO CHAMADOS POR OBJ
# NAO e uma boa pratica chamar esse tipo de elemento com(_) por fora da class
print(cat._tamanho)  #DEVERIA DAR ERROR/ ELEMENTOS PROTEGIDOS NAO SAO CHAMADOS POR OBJ