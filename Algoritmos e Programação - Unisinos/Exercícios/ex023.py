# Exercício 23 - Índice de Massa Corporal 

nome = str(input("Digite o seu nome: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f"""
          Nome: {nome}
          IMC: {IMC:.2f}
          Classificação: Abaixo do Peso
          """)
elif IMC >= 18.5 and IMC <= 24.9: 
    print(f"""
          Nome: {nome}
          IMC: {IMC:.2f}
          Classificação: Peso Normal
          """)
elif IMC >= 25 and IMC <= 29.9:
    print(f"""
          Nome: {nome}
          IMC: {IMC:.2f}
          Classificação: Pré-obesidade
          """)
elif IMC >= 30 and IMC <= 34.9:
    print(f"""
          Nome: {nome}
          IMC: {IMC:.2f}
          Classificação: Obesidade Grau 1
          """)
elif IMC >= 35 and IMC <= 39.9:
    print(f"""
          Nome: {nome}
          IMC: {IMC:.2f}
          Classificação: Obesidade Grau 2
          """)
else: 
    print(f"""
          Nome: {nome}
          IMC: {IMC:.2f}
          Classificação: Obesidade Grau 3
          """)