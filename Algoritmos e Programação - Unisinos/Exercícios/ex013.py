# Exercício 13 - Divisão

A = int(input("Digite um número: "))
B = int(input("Digite outro número: "))

def divAB(A,B):
    return A / B

if B > 0:
    print(f"A divisão de {A} por {B} é: {divAB(A,B):.2f}!")
elif B < 1:
    print("Erro! Tente novamente!")