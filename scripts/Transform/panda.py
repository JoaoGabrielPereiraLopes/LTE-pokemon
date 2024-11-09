import sqlite3 as sql3
import pandas as pd
import os

# Caminho para o arquivo CSV
caminho_arquivo = os.path.join('../../database', 'Pokemon.csv')

# Caminho absoluto para o arquivo
nome_csv = os.path.abspath(caminho_arquivo)
nome_banco = os.path.abspath('../../database/Pokemon.db')

# Conectando ao banco e importando o CSV usando pandas
conexao = sql3.connect(nome_banco)
df = pd.read_csv(nome_csv)

# Criando a tabela 'types' no banco de dados
types = pd.DataFrame(df['Type 1'].unique(), columns=['Type 1'])
types.rename(columns={'Type 1': 'type'}, inplace=True)
types.reset_index(inplace=True)
types.rename(columns={'index': 'id'}, inplace=True)

# Exportando a tabela 'types' para o banco de dados
types.to_sql('types', conexao, if_exists='replace', index=False)

# Criando a tabela 'generation' no banco de dados
generation = pd.DataFrame(df['Generation'].unique(), columns=['Generation'])
generation.reset_index(inplace=True)
generation.rename(columns={'index': 'id'}, inplace=True)
generation.to_sql('generation', conexao, if_exists='replace', index=False)

# Atualizando as gerações no dataframe
consulta = '''SELECT id, Generation FROM generation;'''
ids = pd.read_sql_query(consulta, conexao)
for x in ids['id']:
    y = ids[ids['id'] == x]['Generation'].iloc[0]
    df.loc[df['Generation'] == y, 'Generation'] = x

# Atualizando os tipos no dataframe
consulta = '''SELECT id, type FROM types;'''
ids = pd.read_sql_query(consulta, conexao)

# Recarregando o CSV original para atualizar os tipos
pk = pd.read_csv(nome_csv)
for x in ids['id']:
    y = ids[ids['id'] == x]['type'].iloc[0]
    pk.loc[pk['Type 1'] == y, 'Type 1'] = x
    pk.loc[pk['Type 2'] == y, 'Type 2'] = x

# Substituindo valores NaN em 'Type 1' e 'Type 2' por string vazia
pk.loc[pk['Type 1'].isna(), 'Type 1'] = ''
pk.loc[pk['Type 2'].isna(), 'Type 2'] = ''

# Remover Pokémon com nome que contém "Mega"
pk1 = pk[~pk['Name'].str.contains('Mega ', case=False, na=False)]

# Selecionando as colunas que você quer
pk1 = pk1[['Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']]

# Resetando o índice e renomeando a coluna de índice
pk1.reset_index(inplace=True)
pk1.rename(columns={'index': 'id'}, inplace=True)

# Atualizando a coluna 'Generation' no DataFrame pk1 com os IDs correspondentes
for index, row in generation.iterrows():
    pk1.loc[pk1['Generation'] == row['Generation'], 'Generation'] = row['id']

# Salvando o DataFrame final na tabela 'pokemon'
pk1.to_sql('pokemon', conexao, if_exists='replace', index=False)

# Filtrando Pokémon Mega
pk2 = pk[pk['Name'].str.contains('Mega ')]
pk2.drop(columns=['Generation', 'Legendary'], inplace=True)

# Consulta para pegar os ids dos Pokémon
consulta = '''SELECT id, Name FROM pokemon;'''
ids = pd.read_sql_query(consulta, conexao)

# Atualizando as Mega Evoluções
for index, row in pk2.iterrows():
    mega_name = row['Name']
    original_name = mega_name.split(' ')[1]  # Pegando o nome do Pokémon original
    # Buscando o id do Pokémon original
    original_id = int(pk1[pk1['Name'] == original_name]['id'].iloc[0])
    
    # Atualizando o nome do Pokémon Mega
    new_name = ''.join(mega_name.split(' ')[1:])  # Removendo a palavra "Mega" do nome

    pk2.at[index, 'Name'] = new_name  # Atualizando o nome no DataFrame
    pk2.at[index, 'original'] = original_id  # Associando o id do Pokémon original

# Salvando as Mega Evoluções no banco
pk2.to_sql('Mega', conexao, if_exists='replace', index=False)

# Fechando a conexão com o banco de dados
conexao.close()
