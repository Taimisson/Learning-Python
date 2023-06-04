# Aula 22 - Módulos e Pacotes

# from uteis import fatorial, dobro
from uteis import numbers

# Programa principal
num = int(input("Digite um valor: "))
fat = numbers.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numbers.dobro(num)}")
