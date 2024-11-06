import sqlite3 as sql3
import pandas as pd
import os

caminho_arquivo = os.path.join('../../database', 'Pokemon.csv')
caminho_absoluto = os.path.abspath(caminho_arquivo)

class Mega:
    def __init__(self,registro,nome_original):
        with sql3.connect('../../database/pokemon.db') as conexao:
            self.cursor = conexao.cursor()
            self.pokemon = self.cursor.execute(f'SELECT ID FROM pokemon WHERE NAME == "{nome_original}";').fetchone()[0]

            self.cursor.execute('INSERT INTO mega (NAME, TYPE1, TYPE2, TOTAL, HP, ATTACK, DEFENSE, SP_ATAQUE, SP_DEFENSE, SPEED, POKEMON) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
        (registro['name'], registro['type1'], registro['type2'],
        registro['total'], registro['hp'], registro['attack'],
        registro['defense'], registro['sp ataque'],
        registro['sp defense'], registro['speed'],
        self.pokemon))


def registrador_mega():
    dados = pd.read_csv(caminho_absoluto)
    dados = pd.DataFrame(dados)
    dados_mega = dados[dados['Name'].str.contains('Mega ')]
    for _,x in dados_mega.iterrows():
        registro={
            'name':x['Name'].split(' ')[0],
            'type1':x['Type 1'],
            'type2':x['Type 2'],
            'total':x['Total'],
            'hp':x['HP'],
            'attack':x['Attack'],
            'defense':x['Defense'],
            'sp ataque':x['Sp. Atk'],
            'sp defense':x['Sp. Def'],
            'speed':x['Speed']
        }
        nome_original=x['Name'].split(' ')[1]
        inserir=Mega(registro,nome_original)