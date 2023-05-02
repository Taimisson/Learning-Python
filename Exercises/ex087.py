# Exercício 87

matriz = [ [ 0, 0, 0] , [ 0, 0, 0] , [ 0, 0, 0] ]
soma_pares = 0
maior_valor = 0

for L in range(3):
    for C in range(3):
        matriz[L][C] = int(input(f"Digite um valor na posição {[L]},{[C]}: "))
        if matriz[L][C] % 2 == 0: # Soma dos valores pares da matriz
            soma_pares += matriz[L][C]  
        if matriz[1][C] > maior_valor: # Maior valor da segunda linha
            maior_valor = matriz[1][C]    
 
 
 # Printa a matriz
print()
for L in range(3):
    for C in range(3):
        print(f"[{matriz[L][C]:^5}]", end=" ")
    print()
    
# Outros dados
soma_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]  
print()
print(f"A soma dos pares é {soma_pares}.")
print(f"A soma dos valores da terceira coluna é {soma_coluna}.")
print(f"O maior valor da segunda linha é {maior_valor}.")