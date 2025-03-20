class select:
    def by_id(self):
        print('Selecionando um elemento no BD')

class insert:
    def inser_value(self):
        print('Inserindo um valor no BD')

class repositorio:
    def __init__(self): # e uma usabilidade direta
        self.__select = select()  #COMPOSIÇÃO
        self.__insert = insert()
        pass

    def select_by_id(self, id: int):
        self.__select.by_id()

repo = repositorio()
repo.select_by_id(22) 