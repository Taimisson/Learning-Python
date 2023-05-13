# Exercício 91

# Importando 
from random import randint
from operator import itemgetter

# Criando dicionário do Jogo
jogoDado = {
    "Jogador1": randint(1,6),
    "Jogador2": randint(1,6),
    "Jogador3": randint(1,6),
    "Jogador4": randint(1,6)
}

# Printando em ordem com .items() para dicionário
for k, v in jogoDado.items():
    print(f"O {k} tirou {v}.")
    
print()    
print(" = = O ranking dos jogadores = =")

# Colocando o dicionário em ordem usando itemgetter
ranks = {}
ranks = sorted(jogoDado.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranks):
    print(f"O {i+1}º lugar: {v[0]} com {v[1]}.")