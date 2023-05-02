# Exercício 85

# numeros = []
# pares = []
# impares = []

# for i in range(7):
#     numeros.append(int(input(f"Digite o {i}º valor: ")))
#     if len(numeros) >= i+1 and numeros[i] % 2 == 0:
#         pares.append(numeros[i])
#     elif len(numeros) >= i+1:
#         impares.append(numeros[i])
    

# pares.sort()
# impares.sort()


# print(f"Os valores pares digitados foram: {pares}")
# print(f"Os valores impares digitados foram: {impares}")

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else: 
        num[1].append(valor)

num[0].sort()
num[1].sort()

print(f"Os valores pares digitados foram: {num[0]}")
print(f"Os valores impares digitados foram: {num[1]}")
