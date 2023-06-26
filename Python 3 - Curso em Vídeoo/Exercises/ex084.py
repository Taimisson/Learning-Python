# Exercício 84

temp = []
pessoas = []
mai = men = 0

while True:
    temp.append(str(input("Qual o seu nome? ")))
    temp.append((input("Qual seu peso? ")))
    # if len(pessoas) == 0:
    #     mai = men = temp[1]
    # else:
    #     if temp[1] > mai:
    #         mai = temp[1]
    #     if temp[1] < men:
    #         men = temp[1]
    
    pessoas.append(temp[:])
    temp.clear() # Limpar ou ficará duplicada
    
    r = str(input("Deseja continuar? [S/N] ")).upper()
    if r.startswith("N"):
        break 

# print(f"Foram cadastradas {len(pessoas)} pessoas.")
# print(f"O maior peso foi de {mai}Kg. Peso de ", end="")
# for p in pessoas:
#     if p[1] == mai:
#         print(f"[{p[0]}] ", end="")
# print(f"O menor peso foi {men}Kg. Peso de ", end="")
# for p in pessoas:
#     if p[1] == men:
#         print(f"[{p[0]}] ", end="")
    
print(f"Foram cadastradas {len(pessoas)} pessoas.")
maior_peso = max(p[1] for p in pessoas)
print(f"O maior peso foi de {maior_peso}Kg. Peso de ", end="")
for nome, peso in pessoas:
    if peso == maior_peso:
        print(f"[{nome}], ", end="")

print("\n")

menor_peso = min(p[1] for p in pessoas)
print(f"O menor peso foi {menor_peso}Kg. Peso de ", end="")
for nome, peso in pessoas:
    if peso == menor_peso:
        print(f"[{nome}], ", end="")

print("\n")