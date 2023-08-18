# Exercício 25 - Jogo de Par ou Ímpar

jogadorUmNome = str(input("Digite o nome do 1ª jogador: "))
jogadorDoisNome = str(input("Digite o nome do 2ª jogador: "))

jogadorUmOpcao = str(input("1º Jogador: Par ou Ímpar? ")).lower()

jogadorUmValor = int(input("1º Jogador! Digite um número inteiro: "))
jogadorDoisValor = int(input("2º Jogador! Digite um número inteiro: "))

valor = jogadorUmValor + jogadorDoisValor

if jogadorUmOpcao == "par" and valor % 2 == 0:
    print(f"RESULTADO: {valor}! O jogador {jogadorUmNome} ganhou!")
else:
    print(f"RESULTADO: {valor}! O jogador {jogadorDoisNome} ganhou!")
    