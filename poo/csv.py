import csv
from dataclasses import dataclass

@dataclass
class CsvHandler:
    nome_arquivo: str
    delimitador: str = ','

    def ler_csv(self):
        dados = []
        with open(self.nome_arquivo, 'r', encoding= 'utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo, delimiter=self.delimitador)
            for linha in leitor_csv:
                dados.append(linha)
        return dados 
    
    def exibir_dados(self, dados):
        for linha in dados:
            print(linha)

#PARA USAR A CLASSE 

manipular_csv = CsvHandler(nome_arquivo='dados.csv')
dados_lidos = manipular_csv.ler_csv()
manipular_csv.exibir_dados(dados_lidos)