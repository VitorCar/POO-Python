#Herança
#Crie uma classe View com:

#étodo render() que imprime "Renderizando view base"

#Crie duas subclasses:

#HomeView, que sobrescreve render() com "Renderizando página inicial"

#ContatoView, que sobrescreve render() com "Renderizando página de contato"
from time import sleep

class View:
    def render(self):
        print('Renderizando view base')

class HomeView(View):
    def render(self):
        print("Renderizando página inicial")

class ContatoView(View):
    def render(self):
        print("Renderizando página de contato")

v_1 = View()
v_2 = HomeView()
v_3 = ContatoView()

list = [v_1, v_2, v_3]
for v in list:
    v.render()
    sleep(2)