# Exercício 16 - Ano bissexto 

def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
    
def main():
    ano = int(input("Digite um ano: "))

    if ano_bissexto(ano):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")
        
if __name__ == "__main__":
    main()