# Números perfeitos

# Sabendo disto, crie um programa que recebe vários inteiros pelo teclado e, para cada um deles, imprime na tela se ele é ou não um número perfeito. Quando o usuário digitar um número negativo, seu programa deve terminar.



while True:
    
    try:
        num = int(input("Digite um número: "))
        if num < 0:
            break
        
        divisores = []
        
        for i in range(1, num):
            if num % i == 0:
                divisores.append(i)
                
        soma_divisores = sum(divisores)
        
        if num == 0:
            print("O número digitado foi 0")
        elif soma_divisores == num:
            print("O número é perfeito!")
        else:
            print("O número não é perfeito!")
            
    except ValueError:
        print("Valor inválido, tente novamente!")
    
print(f"O número digitado é negativo, programa encerrado!")