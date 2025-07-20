# Herança + Polimorfismo
# Crie uma classe Arquivo com método abrir(), que imprime "Abrindo arquivo genérico...".

# Crie duas subclasses:

# Imagem, que sobrescreve abrir() com "Abrindo imagem..."

# Documento, que sobrescreve abrir() com "Abrindo documento..."

# Crie uma lista com objetos das subclasses e chame abrir() para cada item.
from time import sleep

class Arquivo:
    def abrir(self):
        print('Abrindo arquivo genérico...')

class Imagem(Arquivo):
    def abrir(self):
        print("Abrindo imagem...")

class Documento(Arquivo):
    def abrir(self):
        print("Abrindo documento...")

arquivo_1 = Arquivo()
arquivo_2 = Imagem()
arquivo_3 = Documento()

lista_arquivo = [arquivo_1, arquivo_2, arquivo_3]
for arq in lista_arquivo:
    arq.abrir()
    sleep(1)