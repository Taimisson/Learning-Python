# Exercício 96

def area(largura, comprimento):

    dimensao = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {dimensao}m²")
    
    
 # Programa Principal
 
print("="*30)
print("CONSTROLE DE TERRENOS")
print("="*30)
larg = float(input("Largura (m): "))
comp = float(input("Comprimento (m): "))
area(larg, comp)