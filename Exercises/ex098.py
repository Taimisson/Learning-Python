# Exercício 98

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f"Contagem de {i} até {f} de {p} em {p}")

    if i <= f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="")
            cont += p
        print("FIM")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end="")
            cont -= p
        print("FIM!")

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é a sua vez!")

inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
