# Exercício 24 - Calcular Triângulos

a = int(input("Digite um valor inteiro: "))
b = int(input("Digite um outro valor inteiro: "))
c = int(input("Digite um mais um valor inteiro: "))

if ( abs(b - c)  < a < b + c) and (  abs(a - c) < b < a + c) and ( abs(a - b)  < c < a + b):
    print("NÃO FORMA UM TRIÂNGULO!")
else:
    if a == b == c:
        print("TRIÂNGULO EQUILÁTERO!")
    elif a != b != c:
        print("TRIÂNGULO ESCALENO!")
    else:
        print("TRIÂNGULO ISÓSCELES!")
