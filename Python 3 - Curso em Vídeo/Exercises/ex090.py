# Exercício 90

aluno = {}

# Guarda o nome e a média do aluno em um dicionário
aluno["Nome"] = str(input("Aluno: "))
aluno["Média"] = float(input("Média: "))


# Situação do aluno
if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
elif 5 <= aluno["Média"] < 7:
    aluno["Situação"] = "Recuperação"
else: 
    aluno["Situação"] = "Reprovado"
    
# Printa o nome
for k, v in aluno.items():
    print(f"{k} é igual a {v}")
