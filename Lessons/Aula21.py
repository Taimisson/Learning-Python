# Funções (Parte 2)

from time import sleep

def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    Args:
        i (int): Início da contagem
        f (int): Fim da Contagem
        p (int): Passo da contagem
    """
    c = 1
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("FIM")
    
help(contador)

# Docstrings explicam o código, de uma função por exemplo