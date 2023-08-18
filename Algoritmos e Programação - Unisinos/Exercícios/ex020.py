# Exercício 20 - Produto e Preço

nomeProduto = str(input("Digite o nome do Produto: "))
precoProduto = float(input("Digite o preço do Produto: R$"))

compra = int(input(f"Compra do produto: {nomeProduto}! Digite a quantidade: "))

valorTotal = precoProduto * compra

print(f"O valor total da compra deu: R${valorTotal:.2f}!")