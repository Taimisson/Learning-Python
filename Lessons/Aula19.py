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

filme = {
    'titulo': "Star Wars",
    'ano': 1977,
    'diretor': "George Lucas"
}

print(filme.values()) # Valores do dict
print(filme.keys()) # Titulo / ano / Diretor
print(filme.items()) # Todos

for k, v in filme.items():
    print(f"O {k} é {v}")