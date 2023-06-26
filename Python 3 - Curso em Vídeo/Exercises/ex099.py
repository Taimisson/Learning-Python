# Exercício 99

# def encontrarMaiorValor(* num):
#     cont = maior = 0
#     print("="*30)
#     print("Analisando os valores passados... ")
#     for valor in num:
#         print(f"{valor} ", end="")
#         if cont == 0:
#             maior = valor
#         else:
#             if valor > maior:
#                 maior = valor
#         cont += 1
#     print(f"Foram informados {cont} valores ao todo.")
#     print(f"O maior valor informado foi {maior}.")


def encontrarMaiorValor(*num):
    if num:
        print("="*30)
        print(f"Foram informados {len(num)} valores ao todo.")
        for valor in num:
            print(f"{valor} ", end="")
        maior = max(num)
        print(f"| O maior valor fornecido é {maior}")
    else: 
        print("="*30)
        print("     Nenhum valor fornecido")
    


encontrarMaiorValor(2, 9, 4, 5, 7, 1)
encontrarMaiorValor(4, 7, 0)
encontrarMaiorValor(1, 2)
encontrarMaiorValor(6)
encontrarMaiorValor()
