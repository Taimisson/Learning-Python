# Listas (Parte 2)

dados = list()
dados.append("Taimisson")
dados.append(19)
print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:])

pessoas = [["Pedro",25], ["Maria",19], ["João",32]] # Listas compostas

print(pessoas[0][0])    #Pedro
print(pessoas[1][1])    #19
print(pessoas[2][0])    #João
print(pessoas[1])       #["Maria",19]

