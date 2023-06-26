# Exercício 103

def ficha(nome='desconhecido', gols=0):
    print(f"O jogador {nome} fez {gols} gols no campeonato.")

#Programa principal
nomeJogador = str(input("Nome do jogador: "))
numeroGols = input("Número de gols: ")

if nomeJogador == "":
    nomeJogador = "<desconhecido>"

if numeroGols == "":
    numeroGols = 0

ficha(nomeJogador, numeroGols)

