# Contador de Instâncias
# Crie uma classe Aluno que conte quantas instâncias foram criadas.
# Implemente um método total_alunos() que retorne esse número.

class Aluno:
    cont = 0
    def __init__(self):
        Aluno.cont += 1

   
    def total_aluno(self):
        print(f'Cadastrados: {Aluno.cont} alunos.')

al1 = Aluno()
al2 = Aluno()
al3 = Aluno()

al3.total_aluno()