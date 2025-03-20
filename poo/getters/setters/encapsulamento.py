class minhaclasse:
    def __init__(self, nome, idade):
        self. __nome = nome      # atributos privados
        self. __idade = idade 
        pass

    def get__nome(self): #Obtendo o valor do atributo 'privado'
        return self.__nome
        
    def set__nome(self, nome):  #Modificando o valor do atributo para outro nome
        self.__nome = nome
        
    def get__idade(self):
        return self.__idade
    
    def set__idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            print('Idade invalida')


pessoa = minhaclasse('joao', 32)
print(pessoa.get__nome())
print(pessoa.get__idade())
pessoa.set__nome('maria')
print(pessoa.get__nome())
pessoa.set__idade(20)
print(pessoa.get__idade())