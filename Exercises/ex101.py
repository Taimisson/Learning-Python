# Exercício 101

def voto(ano):
    
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    
    if idade < 16:
        return f"Você tem {idade}: NÃO VOTA"
    elif 16 <= idade < 18 or idade > 65:
        return f"Você tem {idade} anos: VOTO OPCIONAL"
    else:
        return f"Você tem {idade} anos: VOTO OBRIGATÓRIO"
    
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
