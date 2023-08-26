from time import sleep
from math import sqrt

def linha():
    print("=-" * 30)
def tela():
    print(
        f"""    
        Olá, {nome}!
        
        Digite a opção desejada:

        1) Verificar triângulo

        2) Calcular equação do segundo grau

        3) Conferir data

        4) Verificar tamanho do texto

        5) Analisar CPF

        6) Contar caracteres
        
        7) Sair
        
    """)   
def verificarTriangulo():
        print("=-" *30)
        print("""PROGRAMA DE VERIFICAR TRIÂNGULO""")
        print("=-" *30)
        a = int(input("Digite o primeiro valor inteiro: "))
        b = int(input("Digite o segundo valor inteiro: "))
        c = int(input("Digite o terceiro valor inteiro: "))

        if (a < b + c and b < a + c and c < a + b):
            # VERIFICAR O TIPO
            if (a == b and b == c):
                linha()
                print("OS LADOS FORMAM: Triângulo Equilátero.")
                linha()
            elif (a == b or a == c or b == c):
                linha()
                print("OS LADOS FORMAM: Triângulo Isósceles.")
                linha()
            else:
                linha()
                print("OS LADOS FORMAM: Triângulo Escaleno.")
                linha()
        else:
            linha() 
            print("Os lados não formam um triângulo!")
            linha()
        
        sleep(2)             
def equacaoSegundoGrau():
        A = int(input("Digite o valor A: "))
        while A == 0:
            print("O valor A não pode ser zero!")
            A = int(input("Digite o valor A: "))
            
        B = int(input("Digite o valor B: "))
        C = int(input("Digite o valor C: "))
        
        delta = B*B - 4*A*C
        
        if delta < 0:
            linha()
            print("Não foi possível calcular o delta.")
            linha()
        elif delta == 0:
            linha()
            print("Possui apenas uma raiz real")
            x = -B/(2*A)
            print("O lugar zero é:",x)
            linha()
        elif delta > 0:
            raizdelta = sqrt(delta)
            x1 = (-B + raizdelta) / (2 * A)
            x2 = (-B - raizdelta) / (2 * A)
            linha()
            print(f"x' = {x1:.2f} e x'' = {x2:.2f}")
            linha()
        
        sleep(2)   
def conferirData():
        # Aceita apenas anos entre 0 e 2023
        ano = int(input("Digite o ano: "))
        while ano < 0 or ano > 2023:
            print("Ano inválido!")
            ano = int(input("Digite o ano: "))
        
        # Aceita apenas os meses entre 1 e 12
        mes = int(input("Digite o mês: "))
        while mes < 1 or mes > 12:
            print("Mês inválido!")
            mes = int(input("Digite o mês: "))

        if mes in [1, 3, 5, 7, 8, 10, 12]:
            quantidadeDiasMes = 31
        elif mes in [4, 6, 9, 11]:
            quantidadeDiasMes = 30
        elif mes in [2] and ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
            quantidadeDiasMes = 29
        else:
            quantidadeDiasMes = 28
            
        # Aceita apenas os dias permitidos
        dia = int(input(f"Digite o dia (1 até {quantidadeDiasMes}): "))
        while dia < 1 or dia > quantidadeDiasMes:
            print("Inválido! Tente novamente!")
            dia = int(input(f"Digite o dia (1 até {quantidadeDiasMes}): "))
            
        print(f"A data informada foi: {dia}/{mes}/{ano}!")  
        
        sleep(2)      
def tamanhoTexto():      
        texto = str(input("Digite um texto qualquer: "))
        tamanhoTexto = len(texto)
        
        while True:    
            if tamanhoTexto < 5:
                print("O tamanho do texto é muito pequeno!")
                break
            elif tamanhoTexto >= 5 and tamanhoTexto < 16:
                print("O tamanho do texto é médio!")
                break
            elif tamanhoTexto > 15 and tamanhoTexto <= 20:
                print("O tamanho do texto é grande!")
                break
            else: 
                while tamanhoTexto > 20:
                    print("O texto é inválido! Digite novamente: ")
                    texto = str(input("Digite um texto qualquer: "))
                    tamanhoTexto = len(texto)
        
        sleep(2)         
def analisarCPF():
        CPFErros = 0
        
        while CPFErros < 3:
            CPF = input("Digite o seu CPF: ")

            valorCPF = CPF.isdigit()
            tamanhoCPF = len(CPF)
            
            if valorCPF and tamanhoCPF == 11:
                print("CPF Válido!")
                break
            else:
                CPFErros += 1
                if CPFErros == 3:
                    print("3 ERROS CONSECUTIVOS! Programa cancelado...")
                else:
                    print("CPF INVÁLIDO! O CPF deve ter 11 dígitos e conter apenas números!")
        sleep(2) 
def contarCaracteres():
        quantidadeVogais = 0
        quantidadeEspaco = 0 
        quantidadeOutros = 0
        texto = input("Digite um texto: ").lower()
        
        
        vogais = "aeiou"
        
        for letra in texto:
            if letra in vogais:
                quantidadeVogais += 1
            elif letra.isspace():
                quantidadeEspaco += 1
            else:
                quantidadeOutros += 1
        
        print(f"""
              Quantidade de vogais: {quantidadeVogais}
              Quantidade de espaços: {quantidadeEspaco}
              Quantidade de outros caracteres: {quantidadeOutros}
              """)
        sleep(2)
        

nome = str(input("Digite o seu nome: "))
contadorErro = 0

while True:
    
    tela()
    
    menu = int(input("Digite a opção desejada: "))
    
    if menu == 1:       # VERIFICAR TRIÂNGULO
        verificarTriangulo()          
    elif menu == 2:     # EQUAÇÃO DO SEGUNDO GRAU
        equacaoSegundoGrau()
    elif menu == 3:     # CONFERIR DATA
        conferirData()
    elif menu == 4:     # VERIFICAR TAMANHO DO TEXTO
        tamanhoTexto()
    elif menu == 5:     # Analisar CPF   
        analisarCPF()   
    elif menu == 6:     # Contar caracteres
        contarCaracteres()
    elif menu == 7:
        print("Obrigado por utilizar nosso sistema.")
        sleep(3)
        break
    else:
        contadorErro += 1
        if contadorErro == 5:
            print("Parece que você não está entendendo o funcionamento do sistema. Até mais!")
            sleep(3) 
            break
        else:
            print("Opção inválida! Tente novamente.")
            sleep(1) 
        

