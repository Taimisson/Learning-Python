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

def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")
    

contador(5,3,6)
contador(3,2)