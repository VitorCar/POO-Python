#Classe com contador de instâncias
#Crie uma classe Documento:

#Atributo de classe contador que inicia em 0.

# Cada vez que um objeto é criado, incremente contador.

#Mostre o total de documentos criados após criar 5 objetos.

class Documento:
    contador = 0 

    def __init__(self, titulo: str):
        self.titulo = titulo
        Documento.contador += 1

dc_1 = Documento('Relatorio 1')
dc_2 = Documento('Relatorio 2')
dc_3 = Documento('Relatorio 3')
dc_4 = Documento('Relatorio 4')
dc_5 = Documento('Relatorio 5')
dc_6 = Documento('Relatorio 6')

print(f"Total de documentos criados: {Documento.contador}")