# Exercício 14 - Preço do Produto

produto = float(input("Digite o preço de um produto: "))

if produto < 1:
    print("Preço inválido!")
elif produto > 0 and produto < 31:
    print("Preço baixo!")
elif produto > 30 and produto < 51:
    print("Preço médio!") 
else: 
    print("Preço alto!")