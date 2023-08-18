# Exercício 22 - Nome e Senha

nome = str(input("Digite o seu nome: "))
senha = str(input("Digite a sua senha: "))

senhaUsuario = nome + "9876"

if senha != senhaUsuario:
    print("ERRO: Senha incorreta!")
else:
    print("Login realizado com sucesso!")
