# %%
import sqlite3 as sql3
import matplotlib.pyplot as plt

# %%
import sqlite3 as sql3
class geracoes:
    def __init__(self):
        conexao = sql3.connect('../../database/pokemon.db')
        self.cursor = conexao.cursor()
    def gens(self):
        pk_generacion = []
        for x in range(1, 7):
            # Executa a consulta SQL e calcula a porcentagem
            linha = self.cursor.execute("SELECT POKEMONS FROM generation WHERE NUMBERS==?", (x,)).fetchone()
            
            if linha:  # Verifica se há algum resultado
                # Calcula a porcentagem do valor POKEMONS
                porcentagem = (linha[0] / 752) * 100
                pk_generacion.append(porcentagem)  # Adiciona a porcentagem à lista
        return pk_generacion
    def lendarios(self):
        lend_generacion = []
        for x in range(1, 7):
            # Executa a consulta SQL e calcula a porcentagem
            linha = self.cursor.execute(f"SELECT LENGENDARYS FROM generation WHERE NUMBERS=={x}").fetchone()
            
            if linha:  # Verifica se há algum resultado
                # Calcula a porcentagem do valor POKEMONS
                porcentagem = (linha[0] / 59) * 100
                lend_generacion.append(porcentagem)  # Adiciona a porcentagem à lista
        return lend_generacion
    def close(self):
        self.cursor.close()

# Chama a função e imprime o resultado

# %%
geracao=geracoes()
labels = ['1', '2', '3', '4','5','6']
sizes = [x for x in geracao.gens()]  # Porcentagens
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen','red','green']  # Cores para cada fatia

# Criando o gráfico de pizza
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('porcentagem de pokemons em cada geração')
# Igualando o aspecto do gráfico para que ele fique redondo
plt.axis('equal')

# Exibindo o gráfico
plt.show()

# %%
geracao=geracoes()
labels = ['1', '2', '3', '4','5','6']
sizes = [x for x in geracao.lendarios()]  # Porcentagens
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen','red','green']  # Cores para cada fatia

# Criando o gráfico de pizza
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('porcentagem de lendarios em cada geração')
# Igualando o aspecto do gráfico para que ele fique redondo
plt.axis('equal')

# Exibindo o gráfico
plt.show()


