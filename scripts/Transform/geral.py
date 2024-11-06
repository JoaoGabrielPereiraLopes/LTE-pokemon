import Generation
import pokemons
import type
import mega
try:
    Generation.registrador_generation()
    type.registrador_type()
    pokemons.registra_pk()
    mega.registrador_mega()
    print('migração feita com sucesso')
except:
    print(deu ruim)