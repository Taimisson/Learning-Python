# Números positivos e média

numeros = []
while True:
    numero = float(input("Digite um número positivo (ou negativo para sair): "))
    if numero < 0:
        if len(numeros) > 0:
            media = sum(numeros) / len(numeros)
            print(f"Média dos números informados: {media}")
        else:
            print("Nenhum número positivo foi informado.")
        break
    numeros.append(numero)
