import sqlite3 as sql3
import pandas as pd
import os

caminho_arquivo = os.path.join('../../database', 'Pokemon.csv')

# Caminho absoluto para o arquivo
caminho_absoluto = os.path.abspath(caminho_arquivo)
class Generation:
    
    def __init__(self, numbers, pokemons, legendarys, execute=True) -> None:
        # Conexão com o banco de dados
        with sql3.connect('../../database/pokemon.db') as conexao:
            self.cursor = conexao.cursor()
            if execute:
                # Inserção de dados na tabela generation
                self.cursor.execute(
                    "INSERT INTO generation (NUMBERS, POKEMONS, LENGENDARYS) VALUES(?,?,?)",
                    (numbers, pokemons, legendarys)
                )
                conexao.commit()  # Certifique-se de salvar a mudança no banco

    def close(self) -> None:
        # Fechar o cursor após o uso
        self.cursor.close()

    def select(self, campos, verificacoes) -> None:
        # Correção do método de consulta SQL
        query = f"SELECT {campos} FROM generation WHERE {verificacoes}"
        self.cursor.execute(query)
        return self.cursor.fetchall()


def registrador_generation():
    # Carregar os dados do arquivo CSV
    dados = pd.read_csv(caminho_absoluto)
    generations = dados['Generation'].unique()  # Gera uma lista das gerações únicas

    for x in range(1,len(generations)+1):
        # Filtrando pokémons de cada geração
        pokemons = dados.loc[dados['Generation'] == x][~dados['Name'].str.contains('Mega ', case=False, na=False)]
        # Filtrando pokémons lendários de cada geração
        lendario = dados.loc[dados['Generation'] == x][~dados['Name'].str.contains('Mega ', case=False, na=False)]
        lendario = lendario[lendario['Legendary'] == True][~dados['Name'].str.contains('Mega ', case=False, na=False)]  # Filtra apenas os lendários

        # Criando o objeto Generation e inserindo dados no banco
        generaton_obj = Generation(x, len(pokemons), len(lendario))
        # Fechando o objeto após a inserção
        generaton_obj.close()