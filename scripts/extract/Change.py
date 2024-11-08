class geracoes:
    def __init__(self):
        
        conexao = sql3.connect('../../database/Pokemon.db')
        self.cursor = conexao.cursor()
        self.geracoes= self.cursor.execute('SELECT count(id) FROM generation;').fetchone()[0]
    def gens(self):
        qtd = self.cursor.execute('SELECT COUNT(*) FROM pokemon WHERE Legendary == TRUE;').fetchone()[0]  # Fetch count value properly
        
        pk_generacion = []
        

        for x in range(1,self.geracoes+1):
            consulta=self.cursor.execute(f"SELECT id FROM generation where Generation=={x};").fetchone()[0]
            # Count the number of Pokémon for each generation
            linha = self.cursor.execute(f"SELECT COUNT(*) FROM pokemon WHERE Generation = {consulta}").fetchone()[0]

            if linha:  # Verifica se há algum resultado
                # Calculate the percentage of Pokémon in this generation
                porcentagem = (linha / qtd) * 100
                pk_generacion.append(porcentagem)

        return pk_generacion
    def lendarios(self):
        lend_generacion = []
        qtd = self.cursor.execute('SELECT COUNT(*) FROM pokemon WHERE Legendary == TRUE;').fetchone()[0]  # Fetch count value properly
        for x in range(1,self.geracoes+1):
            consulta=self.cursor.execute(f"SELECT id FROM generation where Generation=={x};").fetchone()[0]
            # Executa a consulta SQL e calcula a porcentagem
            linha = self.cursor.execute(f"SELECT COUNT(*) LENGENDARYS FROM pokemon WHERE Generation=={consulta} and Legendary==TRUE").fetchone()[0]
            if linha:  # Verifica se há algum resultado
                # Calcula a porcentagem do valor POKEMONS
                porcentagem = (linha / qtd) * 100
                lend_generacion.append(porcentagem)  # Adiciona a porcentagem à lista
        return lend_generacion
    def lends_per_generation(self):
        lista = []
        for x in range(1,self.geracoes+1):
            consulta=self.cursor.execute(f"SELECT id FROM generation where Generation=={x};").fetchone()[0]
            # Contando o total de Pokémon em cada geração
            linha = self.cursor.execute(f"SELECT COUNT(*) FROM pokemon WHERE Generation = {consulta};").fetchone()[0]
            qtd = self.cursor.execute(f"SELECT COUNT(*) FROM pokemon WHERE Legendary == TRUE AND Generation = {consulta};").fetchone()[0]
            if linha > 0:
                lista.append((qtd / linha) * 100)
            else:
                lista.append(0)  # Adiciona 0% se não houver Pokémon na geração
        return lista
    def mega(self):
        mega_generacion = []
        qtd = self.cursor.execute('SELECT COUNT(*) FROM Mega;').fetchone()[0]  # Fetch count value properly
        ids=self.cursor.execute(f"SELECT id FROM Mega;").fetchone()
        ids_generation=self.cursor.execute("SELECT id FROM generation;")
        print(ids_generation)
        gens={}
        for x in ids_generation:
            gens[x[0]]=0
        print(gens)
        for x in ids:
            id_mega= self.cursor.execute(f'SELECT original FROM Mega WHERE id=={int(x)}').fetchone()[0]
            id_generacion_mega= self.cursor.execute(f'SELECT Generation FROM pokemon WHERE id=={id_mega}').fetchone()[0]
            generation_mega=self.cursor.execute(f'SELECT Generation FROM generation WHERE id=={id_generacion_mega}').fetchone()[0]
            # Executa a consulta SQL e calcula a porcentagem
            if generation_mega:  # Verifica se há algum resultado
                # Calcula a porcentagem do valor POKEMONS
                porcentagem = (generation_mega / qtd) * 100
                mega_generacion.append(porcentagem)  # Adiciona a porcentagem à lista
        return mega_generacion
