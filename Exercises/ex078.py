#Exercício 78

num = [] # Lista vazia
for n in range(0,5): 
    num.append(int(input(f"Digite um valor para a Posição {n+1}: ")))
    
max_num = max(num) # encontra o valor máximo da lista
pos_max_num = [] # lista vazia para armazenar as posições do valor máximo

for i, n in enumerate(num): #Loop para encontrar as posições de todos os valores máximos
    if n == max_num:
        pos_max_num.append(str(i+1)) # adiciona a posição como string à lista

min_num = min(num) # encontra o valor mínimo da lista
pos_min_num = [] # lista vazia para armazenar as posições do valor mínimo

for i, n in enumerate(num): #Loop para encontrar as posições de todos os valores mínimos
    if n == min_num:
        pos_min_num.append(str(i+1)) # adiciona a posição como string à lista

# Imprime o resultado para o usuário
print(f'Você digitou os valores {num}.')
print(f'O maior valor digitado foi {max_num} na posição {", ".join(pos_max_num)}')
print(f'O menor valor digitado foi {min_num} na posição {", ".join(pos_min_num)}')
