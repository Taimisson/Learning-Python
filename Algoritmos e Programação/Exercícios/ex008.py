# Exercício 8

praticaA = float(input("Digite a nota da atividade prática do Grau A: "));
teoricaA = float(input("Digite a nota da atividade teórica do Grau A: "));

nota1GA = praticaA * 0.45
nota2GA = teoricaA * 0.55

notaFinalGA = nota1GA + nota2GA

print(f"NOTA FINAL DO GRAU B: {notaFinalGA:.2f}");

provaB = float(input("Digite a nota da prova do Grau B: "));
testeB = float(input("Digite a nota do teste do Grau B: "));
trabalhoB = float(input("Digite a nota do trabalho do Grau B: "));

nota1GB = provaB * 0.60
nota2GB = testeB * 0.20
nota3GB = trabalhoB * 0.20

notaFinalGB = nota1GB + nota2GB + nota3GB

print(f"NOTA FINAL DO GRAU B: {notaFinalGB:.2f}");


notaFinalDisciplina = (notaFinalGA * 0.33) + (notaFinalGB * 0.67)
print(f"NOTA FINAL DA DISCIPLINA: {notaFinalDisciplina:.2f}");


