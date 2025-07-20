# Classe com Métodos de Classe
# Crie uma classe ConfiguracaoApp com atributo de classe modo_escuro.
# Implemente um método de classe alterar_modo(valor) que mude modo_escuro.
# Implemente método exibir_config() que mostre o modo atual.

class ConfiguracaoApp:
    modo_escuro = True

    @classmethod
    def alterar_modo(cls,modo:bool):
        if not isinstance(modo, bool):
            raise TypeError('Somente: True -> (escuro) ou False -> (claro)')
        cls.modo_escuro = modo
        
    @classmethod
    def exibir_config(cls):
        print(f'Modo Escuro = {cls.modo_escuro}')


confg = ConfiguracaoApp()
confg.exibir_config()
confg.alterar_modo(False)
confg.exibir_config()
confg.alterar_modo(12)