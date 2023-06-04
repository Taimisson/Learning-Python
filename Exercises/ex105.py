# Exercício 105

def notas(*notas, situação=False):
    resultado = {}
    resultado["Quantidade de Notas"] = len(notas)
    resultado["Maior nota"] = max(notas)
    resultado["Menor nota"] = min(notas)
    resultado["Média"] = round(sum(notas) / len(notas), 2)
    
    if situação:
        media = resultado["Média"]
        if media >= 7:
            resultado["Situação"] = "Aprovado";
        elif media >= 5:
            resultado["Situação"] = "Recuperação";
        else:
            resultado["Situação"] = "Reprovado";
            
    return resultado
    
    

# Programa principal
resp = notas(5.5, 2.5, 1.5, situação=True)
for key, value in resp.items():
    print(f"{key}: {value}")