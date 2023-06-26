# Exercício 88

# from random import randint

# lista = []
# jogos = []
# num = randint(1, 60)
# quant = int(input("Quantos jogos você deseja fazer? "))
# total = 0

# while total < quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     total += 1
# for i, l in enumerate(jogos):
#     print(f"Jogo {i}: {l:}")
            
import random
for x in range(int(input('Number of games: '))): 
    print(f'Game {x+1}: {random.sample(range(1, 61), 6)}')