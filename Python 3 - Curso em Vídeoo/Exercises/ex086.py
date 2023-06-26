#Exercício 86   

matriz = [ [ 0, 0, 0] , [ 0, 0, 0] , [ 0, 0, 0] ]

for l in range(3): # Linha
    for c in range(3): # Coluna
         matriz[l][c] = int(input(f"Digite um valor para a posição {[l]},{[c]}: "))
         

for l in range(3): # Print Linhas
    for c in range(3): # Print Colunas
        print(f"[{matriz[l][c]:^3}]", end=" ")
    print()

