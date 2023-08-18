# Exerício 28 - Pedra, Papel, Tesoura, Lagarto, Spock

jogador1 = str(input("Digite o nome do primeiro jogador: "))
jogador2 = str(input("Digite o nome do segundo jogador: "))

jogador1jogada = str(input(f"{jogador1} - Digite a sua jogada (pedra, papel, tesoura, lagarto ou spock): ")).lower()
jogador2jogada = str(input(f"{jogador2} - Digite a sua jogada (pedra, papel, tesoura, lagarto ou spock): ")).lower()


# Pedra
if jogador1jogada == "pedra":
    if jogador2jogada == "tesoura" or jogador2jogada == "lagarto":
        print(f"Jogador {jogador1} é o ganhador! {jogador1jogada.upper()} contra {jogador2jogada.upper()}")
    else:
        print(f"Jogador {jogador2} é o ganhador! {jogador2jogada.upper()} contra {jogador1jogada.upper()}")

# Papel
if jogador1jogada == "papel":
    if jogador2jogada == "pedra" or jogador2jogada == "spock":
        print(f"Jogador {jogador1} é o ganhador! {jogador1jogada.upper()} contra {jogador2jogada.upper()}")
    else:
        print(f"Jogador {jogador2} é o ganhador! {jogador2jogada.upper()} contra {jogador1jogada.upper()}")
        
# Tesoura
if jogador1jogada == "tesoura":
    if jogador2jogada == "papel" or jogador2jogada == "lagarto":
        print(f"Jogador {jogador1} é o ganhador! {jogador1jogada.upper()} contra {jogador2jogada.upper()}")
    else:
        print(f"Jogador {jogador2} é o ganhador! {jogador2jogada.upper()} contra {jogador1jogada.upper()}")
        
# Lagarto 
if jogador1jogada == "lagarto":
    if jogador2jogada == "spock" or jogador2jogada == "papel":
        print(f"Jogador {jogador1} é o ganhador! {jogador1jogada.upper()} contra {jogador2jogada.upper()}")
    else:
        print(f"Jogador {jogador2} é o ganhador! {jogador2jogada.upper()} contra {jogador1jogada.upper()}")
        
# Spock
if jogador1jogada == "spock":
    if jogador2jogada == "pedra" or jogador2jogada == "tesoura":
        print(f"Jogador {jogador1} é o ganhador! {jogador1jogada.upper()} contra {jogador2jogada.upper()}")
    else:
        print(f"Jogador {jogador2} é o ganhador! {jogador2jogada.upper()} contra {jogador1jogada.upper()}")   