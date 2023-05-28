# Exercício 99

def encontrarMaiorValor(*num):
    if num:
        print("-"*30)
        print(f"Os valores digitados foram {num}")
        maior = max(num)
        print(f"O maior valor fornecido é {maior}")
    else: 
        print("Nenhum valor fornecido")
    print("-"*30)
    


encontrarMaiorValor(2, 9, 4, 5, 7, 1)
encontrarMaiorValor(4, 7, 0)
encontrarMaiorValor(1, 2)
encontrarMaiorValor(6)
encontrarMaiorValor()
