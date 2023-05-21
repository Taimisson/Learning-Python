# Exercício 94

lista = []
listaMulheres = []
acimaMedia = []

while True:
    
    nome = str(input("Nome: "))
    
    while True:
        sexo = str(input("Sexo: [M/F] ")).upper()[0]
        if sexo in ["M", "F"]:
            break
        else:
            print("Entrada inválida. Digite apenas 'M' ou 'F'!")
            
    idade = int(input("Idade: "))
    
    # Criação do dicionário com as informações da pessoa
    pessoa = {
        "nome": nome,
        "sexo": sexo.upper(),
        "idade": idade
    }
    
    lista.append(pessoa)
    
    if sexo.upper() == "F":
        listaMulheres.append(pessoa)

    while True:
        resposta = input("Quer continuar? [S/N] ").upper()[0]
        if resposta in "SN":
            break
        print("Resposta inválida. Digite apenas 'S' para Sim ou 'N' para Não!")
            
    if resposta == "N":
        break
        
# Obtém o número de pessoas cadastradas contando o tamanho da lista
cont = len(lista) 

# Calcula a soma das idades usando uma expressão geradora
totalIdade = sum(pessoa["idade"] for pessoa in lista) 

# Calcula a média de idade
mediaIdade = totalIdade / cont 

# Impressão dos resultados
print(f"A) Pessoas cadastradas: {cont}")
print(f"B) A média de idade é: {mediaIdade:.2f} anos")

# Lista de mulheres cadastradas
nomesMulheres = ', '.join(pessoa["nome"] for pessoa in listaMulheres)
print("C) As mulheres cadastradas foram:", nomesMulheres)
    
    
# Lista com as pessoas acima da média.
# acimaMedia = [pessoa for pessoa in lista if pessoa["idade"] >= mediaIdade]
    
print("D) Lista das pessoas que estão acima da média: ")
for pessoa in lista:
    if pessoa["idade"] >= mediaIdade:
        print("     ", end="")
        for k, v in pessoa.items():
            print(f"{k}: {v}; ", end="")
        print()

 