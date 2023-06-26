# Exercício 113

def leiaInt(msg):
    while True:
        try:
          n = int(input(msg))  
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return n
        

n = leiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {n}")