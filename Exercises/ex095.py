# Exercício 95

jogador = {}
gols = []
time = []
cod = 0

while True:
    jogador["cod"] = cod
    jogador["nomeJogador"] = str(input("Nome do jogador: "))
    jogador["partidasJogadas"] = int(input(f"Quantas partidas {jogador['nomeJogador']} jogou? "))

    for c in range(jogador["partidasJogadas"]):
        gols.append(int(input(f"Quantos gols na partida {c + 1}? ")))
    
    jogador["gols"] = gols[:]
    jogador["golsTotal"] = sum(gols)
    time.append(jogador)
    
    cod += 1
    
    resposta = str(input("Deseja continuar? [S/N] ")).upper()[0]
    if resposta == "N":
        break
    
print(jogador)