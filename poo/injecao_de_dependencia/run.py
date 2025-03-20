class celular:
    def __init__(self, modelo: str):
        self.modelo = modelo
        pass
    
    def enviar_mensagem(self, msn: str) -> None:
        print(f'Enviando mensagem: {msn}')

    def abrir_emails(self) -> None:
        print('Abrindo emails')

    def abrir_youtube(self) -> None:
        print('Abrindo Youtube...')

class pessoa:  # uma class pessoa esta utilizando uma class celular 
    def __init__(self, celular: celular):  #chamando a classe celualr 
        self.celular = celular  #dependencia class celular
        pass

    def pedir_pizza(self) -> None:  # nao esta sendo apartir de uma entrada depois do self
        print('Buscando o celualr')
        print('Definindo o sabor...')
        # eu estou chamando pela dependencia da classe celular
        self.celular.enviar_mensagem('Quero uma de bacon.')
        print('Aquardando a chegada.')

    def estudar(self):
        print('Sentado no computador')
        self.celular.abrir_youtube()
        print('Anotando o conteudo')

android = celular('samsung')
iphone = celular('iphone')

bastião = pessoa(android)
maria = pessoa(iphone)

bastião.pedir_pizza()
print('-' * 30)
maria.estudar()