# Exercício 102

def fatorial(num, show=False):
    """Calcula o fatorial de um número

    Args:
        num (int): o númeor a ser calculado
        show (bool, optional): Mostrar ou não a conta. Defaults to False.

    Returns:
        fatorial: fatorial do número inserido
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f
    
    # if num == 0:
    #     return 1
    # else:
    #     return num * fatorial(num - 1)
    


print(fatorial(5, show=True))
help(fatorial)
