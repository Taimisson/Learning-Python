# Exercício 83

expr = str(input("Digite a expressão: "))
pilha = []

for simb in expr:
    if simb == "(":
        pilha.append('(')
    elif simb == ')':
        # if len(pilha) > 0: 
        if pilha: # Podemos usar apenas pilha como uma condição, pois a lista vazia é avaliada como False.
            pilha.pop()
        else:
            break
        
if not pilha:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

    