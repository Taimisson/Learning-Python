# Exercício 17 - Menu de Calculadora

def soma():
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    return a + b


def subtracao():
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    return a - b


def multiplicacao():
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    return a * b


def divisao():
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    while b == 0:
        print("Erro: Dividendo não pode ser zero!")
        b = float(input("Digite o dividendo: "))
    return a / b


def potencia():
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    return a ** b


def radiciacao():
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
    if b == 0:
        return "Índice zero não é permitido!"
    return a ** (1/b)


def main():
    while True:
        print("""
Digite 1 para somar dois valores
Digite 2 para subtrair dois valores
Digite 3 para multiplicar dois valores
Digite 4 para dividir dois valores
Digite 5 para realizar uma potência entre dois valores
Digite 6 para realizar uma radiciação entre dois valores
Digite qualquer outro número para sair               
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Resultado da soma: {soma()}")
        elif opcao == "2":
            print(f"Resultado da subtração: {subtracao()}")
        elif opcao == "3":
            print(f"Resultado da multiplicação: {multiplicacao()}")
        elif opcao == "4":
            print(f"Resultado da divisão: {divisao()}")
        elif opcao == "5":
            print(f"Resultado da potência: {potencia()}")
        elif opcao == "6":
            print(f"Resultado da radiciação: {radiciacao()}")
        else:
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
