class geracoes:
    def __init__(self):
        
        conexao = sql3.connect('../../database/Pokemon.db')
        self.cursor = conexao.cursor()
        self.geracoes= self.cursor.execute('SELECT count(id) FROM generation;').fetchone()[0];
    def gens(self):
        qtd = self.cursor.execute('SELECT COUNT(*) FROM pokemon').fetchone()[0]  # Fetch count value properly
        pk_generacion = []

        for x in range(1, 7):
            # Count the number of Pokémon for each generation
            linha = self.cursor.execute("SELECT COUNT(*) FROM pokemon WHERE Generation = ?", (x,)).fetchone()

            if linha:  # Verifica se há algum resultado
                # Calculate the percentage of Pokémon in this generation
                porcentagem = (linha[0] / qtd) * 100
                pk_generacion.append(porcentagem)

        return pk_generacion
    def lendarios(self):
        lend_generacion = []
        qtd = self.cursor.execute('SELECT COUNT(*) FROM pokemon WHERE Legendary == TRUE;').fetchone()[0]  # Fetch count value properly
        for x in range(self.geracoes+1):
            # Executa a consulta SQL e calcula a porcentagem
            linha = self.cursor.execute(f"SELECT COUNT(*) LENGENDARYS FROM pokemon WHERE Generation=={x} and Legendary==TRUE").fetchone()[0]
            if linha:  # Verifica se há algum resultado
                # Calcula a porcentagem do valor POKEMONS
                porcentagem = (linha / qtd) * 100
                lend_generacion.append(porcentagem)  # Adiciona a porcentagem à lista
        return lend_generacion
    def mega(self):
        mega_generacion = []
        qtd = self.cursor.execute('SELECT COUNT(*) FROM Mega;').fetchone()[0]  # Fetch count value properly
        for x in range(self.geracoes+1):
            # Executa a consulta SQL e calcula a porcentagem
            linha = self.cursor.execute(f"SELECT Count(*) FROM pokemon, WHERE
pokemon.fieldID=Mega.foreignkey and Generation=={x};").fetchone()[0]
            if linha:  # Verifica se há algum resultado
                # Calcula a porcentagem do valor POKEMONS
                porcentagem = (linha / qtd) * 100
                mega_generacion.append(porcentagem)  # Adiciona a porcentagem à lista
        return mega_generacion
    def close(self):
        self.cursor.close()
# Chama a função e imprime o resultado
print(geracoes().lendarios())

print(geracoes().mega())
