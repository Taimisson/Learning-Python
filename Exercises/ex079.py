# Exercício 79

num = []
while True:
    valor = (int(input("Digite um valor numérico: ")))
    if valor not in num: # verifica se o valor já está na lista
        num.append(valor) # adiciona o valor à lista se não estiver presente
        print("Valor adicionado com sucesso...")
    else:
        print("Esse valor já está na lista, não será adicionado")
    answer = (str(input("Deseja continuar? [S/N] "))).upper()
    if answer in "N":
        break
    
num.sort()
print(f'Você digitou os valores {num}')
