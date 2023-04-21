# Aula 17 - Listas (Parte 1)

# lanche = ["Hamburguer","Suco","Pizza", "Pudim"]
# lanche[3] = "picolé"

# # Adicionar elementos
# lanche.append("cookie") #Adiciona um item na lista
# lanche.insert(0,"Cachorro-Quente") #Adiciona um item na lista em uma posição indicada

# #Remover elementos
# del lanche[3] # Elimina o elemento, valor e vai refazer os Índices/Contagem
# lanche.pop(3) #Geralmente usado para eliminar o último elemento (Que é o cookie)
# #lanche.remove("Pizza") #Remove você usa o VALOR do elemento
# if "Pizza" in lanche:
#     lanche.remove("Pizza")

# print(lanche)

# #valores = list(range(4,11))

# valores = [8,2,5,4,9,3,0]
# valores.sort() # Ordernar de forma crescente
# valores.sort(reverse=True) # Ordenar de forma decrescente
# len(valores) #Quantidade de valores
# print(valores)
# 

# num = [2,5,9,1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2,2)
# if 4 in num:
#     num.remove(4)
# else:
#     print('Não achei o número')
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = list()
# for cont in range(0,5):
#     valores.append(int(input("Digite uwm valor: ")))


# for c, v in enumerate(valores):
#     print(f'Na possição {c} encontrei o valor {v}!')
# print("Cheguei ao final da lista.")

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
