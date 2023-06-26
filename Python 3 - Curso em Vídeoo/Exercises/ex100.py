# Exercício 100

from random import randint

def sorteia(lista):
    print("------------SORTEANDO...-----------")
    for cont in range(5):
        n = randint(1,10)
        lista.append(n)
        print(f"{n} ", end="")
    print()
      
def somaPar(lista):
    # soma = 0 
    # for num in lista:
    #     if num % 2 == 0:
    #         soma += num
    soma = sum(num for num in lista if num % 2 == 0)
    return soma

# Principal

números = []
sorteia(números)
resultado = somaPar(números)
print(f"Somando os valores pares de {números}, temos {resultado}")

