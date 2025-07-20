# Encapsulamento
# Crie uma classe ConfiguracaoSistema com:

# atributo privado __modo_debug

# propriedade modo_debug com getter e setter (só aceita True ou False)

# método exibir()

class ConfiguracaoSistema:
    def __init__(self, modo_debug: bool):
        self.modo_debug = modo_debug

    @property
    def modo_debug(self):
        return self.__modo_debug
        
    @modo_debug.setter
    def modo_debug(self, new_modo_debug: bool):
        if not isinstance(new_modo_debug, bool):        #Para validar tipo, use isinstance().
            raise TypeError('Somente: True ou False')
        self.__modo_debug = new_modo_debug

    def exibir(self):
        print(f'Modo debug = {self.__modo_debug}')


exemplo = ConfiguracaoSistema(True)
exemplo.exibir()