#Polimorfismo
#Crie uma função processar_renderizacao(view) que receba qualquer objeto View e chame render().
#Teste passando objetos HomeView e ContatoView.

class View:
    def render(self):
        print('Renderizando view base')


class HomeView(View):
    def render(self):
        print("Renderizando página inicial")

class ContatoView(View):
    def render(self):
        print("Renderizando página de contato")


def processar_renderizacao(view):
        view.render()

v1 = View()
processar_renderizacao(v1)