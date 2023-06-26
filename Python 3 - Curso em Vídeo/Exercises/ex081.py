# Exercício 81

# Variáveis
list = []

while True:
    
    list.append(int(input("Digite um número: ")))
    r = str(input("Deseja continuar? [S/N] ")).upper() 
    if r == "N":
        break

    
list.sort(reverse=True) # Ordem decrescente da lista

# Printa o resultado
print(f"Você digitou {len(list)} números!")
print(f"Os valores da lista são {list}!")

if 5 in list: # Verifica se o valor está dentro da lista
    print("O número 5 está dentro da lista")    
else: 
    print("O número 5 não está dentro da lista")
