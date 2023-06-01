# Exercício 104

def leiaInt(msg):
    
    while True:
        num = input(msg)
        if num.isnumeric():
            return num
            break
        else:
            print("ERRO! Você não digitou um número, tente novamente!")

n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")