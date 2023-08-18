# Exercício 26 - Data

ano = int(input("Digite o ano: "))

# Aceita apenas anos entre 0 e 2023
while ano < 0 or ano > 2023:
    print("Ano inválido!")
    ano = int(input("Digite o ano: "))
    
    
mes = int(input("Digite o mês: "))

# Aceita apenas mes entre 1 e 12
while mes < 1 or mes > 12:
    print("Mês inválido!")
    mes = int(input("Digite o mês:"))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    quantidadeDiasMes = 31
elif mes in [4, 6, 9, 11]:
    quantidadeDiasMes = 30
elif mes in [2] and ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
    quantidadeDiasMes = 29
else:
    quantidadeDiasMes = 28
    
dia = int(input(f"Digite o dia (1 até {quantidadeDiasMes}): "))
while dia < 1 or dia > quantidadeDiasMes:
    print("Inválido! Tente novamente!")
    dia = int(input(f"Digite o dia (1 até {quantidadeDiasMes}): "))
    
    
    
    


print(f"A data informada foi: {dia}/{mes}/{ano}!")