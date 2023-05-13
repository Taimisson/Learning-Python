# # Dicionário

# dados = []
# dados.append("Pedro")
# dados.append(25)

# print(dados[0]) # Pedro
# print(dados[1]) # 25

# # Tuplas ()
# # Listas []
# # Dicionários {}

# dados = dict{}
# dados = { "nome": "Pedro", "idade":25}

# print(dados["Nome"]) # Pedro
# print(dados["idade"])

# # Criar novo elemento 
# dados["sexo"] = "M"
# del dados["idade"]

# filme = {
#     'titulo': "Star Wars",
#     'ano': 1977,
#     'diretor': "George Lucas"
# }

# print(filme.values()) # Valores do dict
# print(filme.keys()) # Titulo / ano / Diretor
# print(filme.items()) # Todos

# for k, v in filme.items(): # Para cara key e valor em 
#     print(f"O {k} é {v}")


# pessoas = {
#     'Nome': "Taimisson", 
#     "Sexo": "M",
#     "Idade":19
# }
# # print(f" O {pessoas['nome']} tem {pessoas['idade']} anos.")

# pessoas["Nome"] = "Pedro" # Modificar nome
# pessoas["Peso"] = 50

# for k, v in pessoas.items():
#     print(f"{k} = {v}")

#  --------------------
# Dicionário em lista

# brasil = []

# estado1 = {
#     "UF": "Rio Grande do Sul",
#     "Sigla": "RS"
# }

# estado2 = {
#     "UF": "São Paulo",
#     "Sigla": "SP"
# }

# brasil = []
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[1]["Sigla"])

estado = {}
brasil = []

for c in range(3):
    estado["UF"] = str(input("Digite o nome de um Estado do Brasil: "))
    estado["Sigla"] = str(input("Digite a sigla do Estado: "))
    brasil.append(estado.copy()) # Copiar o dicionário para funcionar e não ficar ligado 

for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()
