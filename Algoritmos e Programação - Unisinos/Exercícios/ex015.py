# Exercício 15 - Taxa de Juros

def aplicar_juros(valor):
    if valor < 0:
        return "Erro! Valor negativo!"
    
    if valor < 100:
        novo_valor = valor * 1.10
    elif valor < 300:
        novo_valor = valor * 1.20 
    elif valor < 1000:
        novo_valor = valor * 1.50 
    else:
        novo_valor = valor 
    
    return novo_valor

def main():
    valor = float(input("Digite o valor: "))
    
    novo_valor = aplicar_juros(valor)
    
    if isinstance(novo_valor, str):
        print(novo_valor)
    else:
        print(f"O valor com juros aplicados é: R${novo_valor:.2f}")

if __name__ == "__main__":
    main()