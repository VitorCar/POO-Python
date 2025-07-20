# Polimorfismo com Animais
# Crie uma classe base Animal com método emitir_som().
# Crie subclasses Gato e Vaca, cada uma implementando emitir_som() de maneira diferente.
# Instancie objetos de cada classe e chame emitir_som().

class Animal:
    def emitir_som(self):
        print('Todo animal emite um som.')

class Gato:
    def emitir_som(self):
        print('O gato: Mia!')

class Vaca:
    def emitir_som(self):
        print('A vaca: Muge!')

gato = Gato()
gato.emitir_som()

vaca = Vaca()
vaca.emitir_som()