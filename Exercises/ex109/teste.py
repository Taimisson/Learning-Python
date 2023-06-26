# Exercício 109

import moeda

# Programa Principal
preço = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}")
print(f"O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(preço, 10, True)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(preço, 13, True)}")
 