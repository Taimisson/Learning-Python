# Exercício 105

def notas(*notas, situação=False):
    """
    Calcula informações sobre notas de alunos.

    Args:
        *notas: Notas dos alunos (número variável de argumentos).
        situacao (bool, opcional): Indica se a situação do aluno deve ser calculada.
                                   O valor padrão é False.

    Returns:
        dict: Dicionário com as seguintes informações:
            - 'Quantidade de notas': Quantidade de notas recebidas.
            - 'Maior nota': Maior nota entre as notas recebidas.
            - 'Menor nota': Menor nota entre as notas recebidas.
            - 'Média da turma': Média das notas recebidas (com duas casas decimais).
            - 'Situação' (opcional): Situação do aluno ('Aprovado', 'Recuperação' ou 'Reprovado').

    """
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
help(notas)