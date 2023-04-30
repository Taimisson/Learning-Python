# Exercício 84

temp = []
pessoas = []
cont = 0

while True:
    temp.append(str(input("Qual o seu nome? ")))
    temp.append((input("Qual seu peso ")))
    pessoas.append(temp[:])
    temp.clear() # Limpar ou ficará duplicada

    r = str(input("Deseja continuar? [S/N] ")).upper()
    if r.startswith("N"):
        break 
    
    

print(pessoas)
print(f"Foram cadastradas {len(pessoas)} pessoas.")
