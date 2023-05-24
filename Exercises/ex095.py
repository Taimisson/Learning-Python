# Exercício 95

time = []
cod = 0

while True:
    jogador = {}
    gols = []
    jogador["Nome"] = str(input("Nome do jogador: "))
    jogador["Partidas"] = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))

    for c in range(jogador["Partidas"]):
        gols.append(int(input(f"Quantos gols na partida {c + 1}? ")))
    
    jogador["Gols"] = gols[:]
    jogador["Total"] = sum(gols)
    time.append(jogador)
    
    resposta = str(input("Deseja continuar? [S/N] ")).upper()[0]
    if resposta == "N":
        break
  
print('cod ', end="")    
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()

for k, v in enumerate(time):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
    
while True:
    buscar = int(input("Mostrar dados de qual jogador? (999 para cancelar) "))
    if buscar == 999:
        break
    if buscar >= len(time):
        print(f"ERRO! Não existe jogador com código {buscar}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[buscar]['Nome']}: ")
        for i, g in enumerate(time[buscar]['Gols']):
            print(f"    No jogo {i + 1} fez {g} gols.")