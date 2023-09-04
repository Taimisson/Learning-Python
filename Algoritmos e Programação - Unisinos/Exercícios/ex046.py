# Exercício 2: Crie um método que recebe 3 notas por parâmetro e retorna o conceito atingido pela média aritmética das notas. Os conceitos são:

# - entre 0.0 e 4.0 (inclusive): conceito "D"
# - entre 4.0 (não incluído) e 7.0 (inclusive): conceito "C"
# - entre 7.0 (não incluído) e 9.0 (inclusive): conceito "B"
# - entre 9.0 (não incluído) e 10.0 (inclusive): conceito "A"

# Caso alguma das notas digitadas seja negativa, retorne o texto "ERRO"


def media_notas(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return "ERRO!"
    else:    
        media = (n1 + n2 + n3) / 3
        
        if media <= 4:
            return f"Média do aluno: {media:.2f} | Conceito: D"
        elif media > 4 and media <= 7:
            return f"Média do aluno: {media:.2f} | Conceito: C"
        elif media > 7 and media <= 9:
            return f"Média do aluno: {media:.2f} | Conceito: B"
        elif media > 9 and media <= 10:
            return f"Média do aluno: {media:.2f} | Conceito: A"
    

print(media_notas(8.1,9,10))
    