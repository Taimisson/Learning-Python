# 2 valores 

val1 = int(input("Digite o primeiro valor inteiro: "))
val2 = int(input("Digite o segundo valor inteiro: "))

if val1 < 0 or val2 < 0:
    print("Pelo menos um dos valores é negativo.")
else:
    menor = min(val1, val2)
    maior = max(val1, val2)
    
    if menor % 2 != 0:
        menor += 1  # Se o menor número for ímpar, aumentamos para o próximo número par
    
    for num in range(menor, maior + 1, 2):
        print(num)

