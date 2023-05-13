# Exercício 90

aluno = {}

# Guarda o nome e a média do aluno em um dicionário
aluno["Nome"] = str(input("Aluno: "))
aluno["Média"] = float(input("Média: "))


# Printa o nome e a média do aluno
print(f"O nome do aluno é {aluno['Nome']}")
print(f"A média do aluno é {aluno['Média']}")

# Média maior ou igual a 7
if aluno["Média"] >= 7:
    print("O aluno foi aprovado!")
else:
    print("O aluno foi reprovado!")