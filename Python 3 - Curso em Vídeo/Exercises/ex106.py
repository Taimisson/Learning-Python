# Exercício 106

c = ('\033[m',          # 0 - SEM CORES
     '\033[0;30;41m',   # 1 - VERMELHO
     );

def ajuda(com):
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("=" * tam)
    print(msg)
    print("=" * tam)
    print(c[0], end="")


# Programa principal
comando = ""
while True:
    título("SISTEMA DE AJUDA PyHELP",)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
título("ATÉ LOGO!",)