#Classe com Sobrecarga de __len__
#Crie uma classe Arquivo:

#Atributo conteudo (str).

#Sobrecarga de __len__ que retorna o número de caracteres.

class Arquivo:
    def __init__(self, texto: str):
        self.texto = texto

    def __len__(self):
        return len(self.texto)
    
    def __str__(self):
        return f'texto = {self.texto}\nCaracteres = {len(self.texto)}'
        
arquivo_1 = Arquivo('Vai dar tudo certo vitor!')
print(arquivo_1)

arquivo_2 = Arquivo('vitor')
print(arquivo_2)