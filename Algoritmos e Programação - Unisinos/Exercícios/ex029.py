# Exercício 29 - Carteira de Motorista

idade = int(input("Digite a sua idade: "))
contador = 0

if idade >= 18:
    primeiraOpcao = str(input("""
1  – Ao prestar socorro à vítima de um acidente, NÃO se deve:

a) acionar imediatamente o Corpo de Bombeiros
b) dar água, comida ou qualquer substância para a vítima cheirar
c) conversar com a vítima para saber de suas condições gerais
d) deixar a vítima confortável até a chegada do socorro especializado

Selecione a opção: """))
    if primeiraOpcao == "b":
        contador += 1
    
    segundaOpcao = str(input("""
2 – Ao se deparar com uma sinaleira na cor vermelha, você deve:

a) rir dela
b) passar mais rápido, pois é perigoso parar
c) dobrar a direita, pois vermelho indica direita
d) parar

Selecione a opção: """))
    if segundaOpcao == "d":
        contador += 1
    
    terceiraOpcao = str(input("""
3 – Segundo a direção defensiva, quando você está em uma via e um pedestre vai atravessar você:

a) buzina muito forte para que o pedestre se assuste
b) atropela o pedestre, pois lugar de pedestre é na calçada
c) para e dá uma carona para o pedestre, pois é uma lei de trânsito
d) para e aguarda ele atravessar
Selecione a opção: """))
    if terceiraOpcao == "d":
        contador += 1
        
    if contador >= 2:
        print("Parabéns, você está apto(a) para tirar a Carteira de Motorista!")
    else: 
         print("Infelizmente você não está apto(a) para tirar a Carteira de Motorista!")
else:
    print("Você não tem idade suficiente para tirar a Carteira de Motorista!")
    

    
