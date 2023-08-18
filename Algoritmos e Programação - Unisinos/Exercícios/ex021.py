# Exercício - Desconto do Produto


nomeProduto = str(input("Digite o nome do Produto: "))
precoProduto = float(input("Digite o preço do Produto: R$"))

compraQnt = int(input(f"Compra do produto: {nomeProduto}! Digite a quantidade: "))

valorTotal = precoProduto * compraQnt

if compraQnt >= 3 and compraQnt <= 4:
    novo_valor = valorTotal - (valorTotal * 0.10)
    print(f"O valor total da compra com desconto de 10% é de: R${novo_valor:.2f}!")
elif compraQnt >= 5 and compraQnt <= 10:
    novo_valor = valorTotal - (valorTotal * 0.15)
    print(f"O valor total da compra com desconto de 15% é de: R${novo_valor:.2f}!")
elif compraQnt >= 10:
    novo_valor = valorTotal - (valorTotal * 0.20)
    print(f"O valor total da compra com desconto de 20% é de: R${novo_valor:.2f}!")
else: 
    novo_valor = valorTotal
    print(f"O valor total da compra é de: R${novo_valor:.2f}!")