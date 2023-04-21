#Aula 17 - Listas (Parte 1)

lanche = ["Hamburguer","Suco","Pizza", "Pudim"]
lanche[3] = "picolé"

# Adicionar elementos
lanche.append("cookie") #Adiciona um item na lista
lanche.insert(0,"Cachorro-Quente") #Adiciona um item na lista em uma posição indicada

#Remover elementos
del lanche[3] # Elimina o elemento, valor e vai refazer os Índices/Contagem
lanche.pop(3) #Geralmente usado para eliminar o último elemento (Que é o cookie)
#lanche.remove("Pizza") #Remove você usa o VALOR do elemento
if "Pizza" in lanche:
    lanche.remove("Pizza")

print(lanche)

#valores = list(range(4,11))

valores = [8,2,5,4,9,3,0]
valores.sort() # Ordernar de forma crescente
valores.sort(reverse=True) # Ordenar de forma decrescente
len(valores) #Quantidade de valores
print(valores)