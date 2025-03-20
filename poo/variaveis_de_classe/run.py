class cachorro:

    tipo = 'canino'   # VARIAVEL DE CLASSE

    def __init__(self, nome):                             
        self.nome = nome        # VARIAVEL DE INSTANCIA
        pass


d = cachorro('Fido')
e = cachorro('Buddy')


print(d.nome)
print(e.nome)
print(d.tipo)
print(e.tipo)
print(cachorro.tipo)

# MUDANDO O VALOR TIPO
cachorro.tipo = 'Erbivoro'
print(d.tipo)
print(cachorro.tipo)

#AlTERAR UM VALOR ESTATICO SOMENTE PARA UM 
d.tipo = 'Felino'
print(d.tipo)