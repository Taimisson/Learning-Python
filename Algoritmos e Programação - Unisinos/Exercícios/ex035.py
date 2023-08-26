# 20 Números flutuantes

numeros = []
i = 0

while i < 20:
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    i += 1
    
numeros_str = ", ".join(map(str, numeros))
print(f"Números digitados: {numeros_str}")