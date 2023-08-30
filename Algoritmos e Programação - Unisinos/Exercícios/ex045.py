# Crie um programa que separa o joio do trigo. Seu programa deve ler a lista abaixo e criar duas listas diferentes: uma com todas as ocorrências da palavra "joio" e outra com todas as ocorrências da palavra "trigo". Ao final, imprima as listas separadas. Copie e cole a linha abaixo no seu código e complete o programa:

joioETrigo = ["joio", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio"]

joios = []
trigos = []

contadorJoio = 0
contadorTrigo = 0


for palavra in joioETrigo:
    if "joio" in palavra:
    # if palavra == "joio":
        joios.append("joio")
        contadorJoio += 1
    elif "trigo" in palavra:
    # elif palavra == "trigo":
        trigos.append("trigo")
        contadorTrigo +=1
        
print(joios)
print(trigos)
print(contadorJoio, contadorTrigo)