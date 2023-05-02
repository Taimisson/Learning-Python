# Exercício 87

matriz = [ [ 0, 0, 0] , [ 0, 0, 0] , [ 0, 0, 0] ]
soma_pares = maior_valor = soma_coluna = 0

# Ler linhas e colunas
for L in range(3):
    for C in range(3):
        matriz[L][C] = int(input(f"Digite um valor na posição {[L]},{[C]}: "))
        
        # Soma dos valores pares da matriz
        if matriz[L][C] % 2 == 0: 
            soma_pares += matriz[L][C]  
        
        # Maior valor da segunda linha
        if matriz[1][C] > maior_valor: 
            maior_valor = matriz[1][C]    
            
# Soma da terceira coluna
for L in range(3): 
    if matriz[L][2]:
        soma_coluna += matriz[L][2]
     
 # Printa a matriz
print()
for L in range(3):
    for C in range(3):
        print(f"[{matriz[L][C]:^5}]", end=" ")
    print()
    
    
# Outros print
soma_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]  
print()
print(f"A soma dos pares é {soma_pares}.")
print(f"A soma dos valores da terceira coluna é {soma_coluna}.")
print(f"O maior valor da segunda linha é {maior_valor}.")