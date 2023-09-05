#Exercício 8: Crie um método que recebe uma lista por parâmetro (assuma que será uma lista de string) e retorna a menor string da lista (com menos caracteres).

def menor_string(lista):
    stringLista = lista[0]
    
    for string in lista:
        if len(string) < len(stringLista):
            stringLista = string
        
    return stringLista

teste = menor_string(["tai","taiso", "taisoooooooo", "taisooo", "taimisson", "taissonnn"])

print(teste)
        
            