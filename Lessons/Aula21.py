 # Funções (Parte 2)

# from time import sleep


# # Docstrings
# def contador(i, f, p):
#     """
#     Faz uma contagem e mostra na tela.
#     Args:
#         i (int): Início da contagem
#         f (int): Fim da Contagem
#         p (int): Passo da contagem
#     """
#     c = 1
#     while c <= f:
#         print(f"{c}", end="..")
#         c += p
#     print("FIM")

# help(contador)

# def somar(a=0, b=0, c=0): # Se o C não for informado, C receberá 0
#     soma = a + b + c 
#     print(f"A soma vale {soma}")

# somar(3, 2 ,5)
# somar(8, 4)
# somar()

# Escopo de Variáveis

# def teste():
#     x = 8
#     print(f"Na função teste, n vale {n}")
#     print(f"Na função teste, x vale {x}")

# n = 2
# print(f"No programa principal, n vale {n}")
# teste()
# print(f"No programa principal, x vale {x}") | X É UMA VARIÁVEL LOCAL 

# def teste(b):
#     global a
#     b += 4
#     c = 2
#     print(f"A dentro vale {a}")
#     print(f"B dentro vale {b}")
#     print(f"C dentro vale {c}")
    
    
a = 5
# teste(a)
# print(f"A fora vale {a}")

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
    
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(8)
