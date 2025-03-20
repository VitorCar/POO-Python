class pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        pass

    def apresentar(self):
        print(f'Ola meu nome e {self.nome} e tenho {self.idade} anos.')

#AQUI COMEÇA A HENRAÇA
class estudante(pessoa): #VAI HERDA DA CLASS PESSOA
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade) #CONSTRUTOR DA CLASS PAI(PESSOA)
        #SUPER() E USADO PARA SE REFERIR A CLASS PAI
        self.matricula = matricula
        self.curso = curso 

    def apresentar(self):
         print(f'Ola meu nome e {self.nome}, tenho {self.idade} anos, minha matricula e {self.matricula} e curso {self.curso}')

estudante1 = estudante('Karla', 24, '2468', 'Administração')
estudante1.apresentar()

#POSSO COLOCAR MAIS CLASS TAMBEM QUE VAO HERDAR A CLASS PAI (PESSOA)