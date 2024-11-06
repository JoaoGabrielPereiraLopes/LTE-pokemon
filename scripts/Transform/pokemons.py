import sqlite3 as sql3
import pandas as pd
import os

caminho_arquivo = os.path.join('../../database', 'Pokemon.csv')

# Caminho absoluto para o arquivo
caminho_absoluto = os.path.abspath(caminho_arquivo)

class Pokemon:
    def __init__(self, dictionary):
        # Abrir a conexão com o banco de dados
        conexao = sql3.connect('../../database/pokemon.db')
        self.cursor = conexao.cursor()
        
        # Buscar os IDs de TYPE1 e TYPE2 (acessando o valor dentro da tupla)
        self.id_type1 = self.cursor.execute('SELECT ID FROM type WHERE NAME = ?', (dictionary['TYPE1'],)).fetchone()
        self.id_type2 = self.cursor.execute('SELECT ID FROM type WHERE NAME = ?', (dictionary['TYPE2'],)).fetchone()

        # Buscar o ID da geração
        self.generation = self.cursor.execute('SELECT ID FROM generation WHERE NUMBERS = ?', (dictionary['GENERATION'],)).fetchone()

        # Acessando o valor dentro da tupla (cuidando de possíveis valores `None`)
        self.id_type1 = self.id_type1[0] if self.id_type1 else None
        self.id_type2 = self.id_type2[0] if self.id_type2 else None
        self.generation = self.generation[0] if self.generation else None
        
        # Inserir dados na tabela
        self.cursor.execute('''
            INSERT INTO pokemon(NAME, TYPE1, TYPE2, TOTAL, HP, ATTACK, DEFENSE, SP_ATAQUE, SP_DEFENSE, SPEED, GENERATION, LEGENDARY)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', 
            (dictionary['NAME'], self.id_type1, self.id_type2, dictionary['TOTAL'], dictionary['HP'], 
             dictionary['ATTACK'], dictionary['DEFENSE'], dictionary['SP_ATAQUE'], dictionary['SP_DEFENSE'], 
             dictionary['SPEED'], self.generation, dictionary['LEGENDARY'])
        )
        
        # Confirmar a transação
        conexao.commit()
        
        # Fechar o cursor e a conexão
        self.cursor.close()
        conexao.close()  # Não se esqueça de fechar a conexão com o banco

def registra_pk():
    # Carregar o arquivo CSV
    dados = pd.read_csv(caminho_absoluto)

    # Filtrar os dados onde o nome contém 'Mega' (ignorando maiúsculas/minúsculas)
    dados_mega = dados[~dados['Name'].str.contains('Mega ', case=False, na=False)]

    # Para cada linha do DataFrame filtrado, crie um dicionário e registre no banco de dados
    for _, linha in dados_mega.iterrows():
        registro = {
            'NAME': linha['Name'],
            'TYPE1': linha['Type 1'],
            'TYPE2': linha['Type 2'],
            'TOTAL': linha['Total'],
            'HP': linha['HP'],
            'ATTACK': linha['Attack'],
            'DEFENSE': linha['Defense'],
            'SP_ATAQUE': linha['Sp. Atk'],
            'SP_DEFENSE': linha['Sp. Def'],
            'SPEED': linha['Speed'],
            'GENERATION': linha['Generation'],
            'LEGENDARY': linha['Legendary']
        }
        
        # Chama a classe Pokemon para registrar os dados no banco de dados
        Pokemon(registro)

    print("Registros concluídos com sucesso!")