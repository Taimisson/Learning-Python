# Exercício 82

list = []
pares = []
impares = []

while True:
    num = (int(input("Digite um  valor: ")))
    list.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
    r = str(input("Quer continuar? [S/N] ")).upper()
    if r == "N":
        break
    
# for i, v in enumerate(list):
#     if v % 2 == 0:
#         pares.append(v)
#     elif v % 2 == 1:
#         impares.append(v)
    
# Deixa em ordem crescente
list.sort()
pares.sort()
impares.sort()
    
# Printa o resultado
print(f"A lista completa é {list}!")
print(f"A lista de pares é {pares}!")
print(f"A lista de ímpares é {impares}!")

