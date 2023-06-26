# Exercício 93

# Criando a lista e dicionário vazia
jogador = {}
gols = []


jogador["Nome"] = str(input("Nome do Jogador: "))
jogador["Partidas"] = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
for c in range(jogador["Partidas"]):
     gols.append(int(input(f"Quantos gols na partida {c + 1}? ")))
    
jogador["Gols"] = gols[:]    
jogador["Total"] = sum(gols)

print("-" * 30)

print(jogador)

print("-" * 30)

# Printa o dicionário
for k, v in jogador.items():
    print(f"{k} tem valor {v}.")

print("-" * 30)

print(f"O jogador {jogador['Nome']} jogou {jogador['Partidas']} partidas.")

# Use enumerate para lISTAS
for i, v in enumerate(jogador["Gols"]):  
    print(f"    => Na partida {i + 1}, fez {v} gols.")
print(f"Foi um total de {jogador['Total']} gols.")