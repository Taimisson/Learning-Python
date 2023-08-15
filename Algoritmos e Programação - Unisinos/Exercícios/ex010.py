# Exercício 10

A = int(input("Digite o valor A: "));
B = int(input("Digite o valor B: "));
C = int(input("Digite o valor C: "));


delta = (B**2 - (4 * A * C)) ** (1/2)
x1 = (-B + delta) / (2 * A)
x2 = (-B - delta) / (2 * A)

print(f"{A}² {B} {C}")
print(f"x' = {x1} e x'' = {x2}")


