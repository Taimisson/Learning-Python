# Exercício 9

A = float(input("Digite o valor A: "));
B = int(input("Digite o valor B: "));

multX = A * B
divX = A / B 
maisX = A + B
menosX = A - B
elevadoX = A ** B

print("A multiplicado por B é:", multX)
print("A dividido por B é:",divX, ", mas com duas casas decimais é: %.2f" %divX)
print("A mais B é:", maisX,"e A menos B é:", menosX)
print("A elevado a B é:",elevadoX)