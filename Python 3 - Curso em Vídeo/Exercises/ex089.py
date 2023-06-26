# Exercício 89

ficha = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    
    r = str(input("Deseja continuar? [S/N] ")).upper()
    if r[0] == "N":
        break


print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")

for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")


while True:
    alunoNota = int(input("Mostrar notas de qual aluno? (Digite 99 para cancelar) "))
    if alunoNota == 99:
        break
    if alunoNota <= len(ficha) -1:
        print(f"As notas de {ficha[alunoNota][0]} são {ficha[alunoNota][1]}")
        
print("Finalizado!")