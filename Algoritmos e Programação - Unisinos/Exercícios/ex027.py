# Exercício 27 - Conta Corrente Saldo

saldoConta = float(input("Digite o saldo da conta: R$"))

opcao = int(input("""
                  1 - Realizar um saque
                  2 - Realizar um depósito
                  
                  Selecione a opção: """))

if opcao == 1:
    valorSaque = float(input("Digite o valor do saque: R$"))
    if valorSaque < 0 or valorSaque > saldoConta:
        print("ERRO: Operação não foi possível!")
    else:
        print("Operação realizada com sucesso!")
elif opcao == 2:
    valorDeposito = float(input("Digite o valor para depositar: R$"))
    if valorDeposito > 300:
        print("ERRO: Valor de depósito ultrapassou o limite (R$ 300,00)")
    else:
        print("Operação realizada com sucesso!")