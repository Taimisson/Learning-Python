# Funções (Parte 1)

# def mostraLinha():
#     print("-"*30)
    
# mostraLinha()
# print("Teste")
# mostraLinha()

# -------

# def mensagem(msg):
#     print("-"*30)
#     print(msg)
#     print("-"*30)
    
# mensagem("SISTEMA DE ALUNOS")

# -------

# def soma(a,b):
#     print(f" A = {a} e B = {b}")
#     s = a + b
#     print(f"{a} + {b} = {s}")
    
    
# # Programa principal
# soma(b=4, a=5)
# soma(7,2)
# soma(3, 9, 5)

# -------

# def contador(*num):
#     tam = len(num)
#     print(f"Recebi os valores {num} e são ao todo {tam} números")
    

# contador(5,3,6)
# contador(3,2)

# -------

# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         pos += 1


# valores = [7,5,3,5,2]
# dobra(valores)
# print(valores)

# -------

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")

soma(5, 2)
soma(2, 9, 4)