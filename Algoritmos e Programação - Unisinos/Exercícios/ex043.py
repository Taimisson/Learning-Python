# Primos

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print("O número não é primo.")
elif numero <= 3:
    print(f"{numero} é um número primo.")
elif numero % 2 == 0 or numero % 3 == 0:
    print(f"{numero} não é um número primo.")
else:
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            print(f"{numero} não é um número primo.")
            break
        i += 6
    else:
        print(f"{numero} é um número primo.")
