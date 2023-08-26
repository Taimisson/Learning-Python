# Fatorial

numero = int(input("Digite um número inteiro não negativo: "))

if numero < 0:
    print("Número inválido. Digite um número não negativo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é: {fatorial}")
