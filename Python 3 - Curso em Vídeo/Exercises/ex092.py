# Exercício 92

from datetime import datetime

worker = {}

worker["Nome"] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
worker["Idade"] = datetime.now().year - nasc



worker["CTPS"] =  int(input("Carteira de Trabalho (O não tem) "))
if worker["CTPS"] != 0:
    worker["Contratação"] = int(input("Ano de Contratação: "))
    worker["Salário"] = float(input("Salário: R$"))
    worker["Aposentadoria"] = worker["Idade"] + ((worker["Contratação"] + 35) - datetime.now().year)

print("--" *30)
for k, v in worker.items():
    print(f" - {k} tem valor {v}.") 