# Herança Múltipla
# Crie classes Camera e Telefone, cada uma com um método informacao().
# Crie uma classe Smartphone que herde de ambas e implemente informacao() chamando os métodos das superclasses.

class Camera:
    def informacao(self):
        print('Camera Ativado.')

class Telefone:
    def informacao(self):
        print('Telefone Ativado.')

class Smartphone:
    def __init__(self, camera:Camera, telefone:Telefone):
        self.camera = camera
        self.telefone = telefone

    def informacao(self):
        self.camera.informacao()
        self.telefone.informacao()
        print('Smartphone Completo.')

minha_camera = Camera()
meu_telefone = Telefone()
celular = Smartphone(minha_camera, meu_telefone)
celular.informacao()
#📦 Composição = um objeto é feito a partir de outros objetos.

