# Somas

inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

soma_pares = 0
soma_impares = 0

for num in range(inicio, fim + 1):
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

print(f"Soma dos valores pares: {soma_pares}")
print(f"Soma dos valores ímpares: {soma_impares}")
