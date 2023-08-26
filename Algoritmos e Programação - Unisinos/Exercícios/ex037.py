# Positivo, Negativo ou Zero

quant = int(input("Digite a quantidade de números a serem digitados: "))
i = 0
while i < quant:
    numero = int(input("Digite um número inteiro: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    i += 1
