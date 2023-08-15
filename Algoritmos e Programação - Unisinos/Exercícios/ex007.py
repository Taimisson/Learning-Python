trabalho = float(input("Digite a nota do trabalho: "))
nota1 = trabalho * 0.10

prova = float(input("Digite a nota da prova: "))
nota2 = prova * 0.60 

teste = float(input("Digite a nota do teste: "))
nota3 = teste * 0.30

notaFinal = nota1 + nota2 + nota3

print("NOTA FINAL DO ALUNO:", notaFinal)