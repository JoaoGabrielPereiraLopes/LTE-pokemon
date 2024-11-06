import sqlite3 as sql3
import pandas as pd
class Type:
    def __init__(self, nome, executar=True) -> None:
        # Conectar ao banco de dados
        conexao = sql3.connect('../../database/pokemon.db')
        self.cursor = conexao.cursor()
        
        # Inserir nome na tabela 'type', se 'executar' for True
        if executar:
            self.cursor.execute("INSERT INTO type (NAME) VALUES (?)", (nome,))
            conexao.commit()  # Commit para garantir que a alteração seja salva no banco de dados
        
        self.conexao = conexao  # Guardando a conexão para usar depois
        
    def select(self, campos, verificacoes):
        # Consultar no banco de dados
        self.cursor.execute(f"SELECT {campos} FROM type WHERE {verificacoes}")
        return self.cursor.fetchall()  # Retorna todos os resultados da consulta

    def close(self):
        # Fechar a conexão quando terminar
        self.conexao.close()

def registrador():
    
    # Ler o arquivo CSV com pandas
    dados = pd.read_csv('C:/Users/gabri/Downloads/LTE-POKEMON-main/database/Pokemon.csv')
    
    # Garantir que dados é um DataFrame
    dados = pd.DataFrame(dados)
    
    # Obter os tipos únicos de 'Type 1'
    types = dados['Type 1'].unique()
    
    # Registrar cada tipo no banco de dados
    for x in types:
        type_obj = Type(x)  # Cria um objeto Type e registra no banco de dados
    
# Chamar a função para registrar
registrador()