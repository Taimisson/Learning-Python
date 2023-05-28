# Exercício 96

def area(largura, comprimento):
    print("="*30)
    print("CONSTROLE DE TERRENOS")
    print("="*30)
    dimensao = largura * comprimento
    print(f"A área de um terreno {largura}x{comprimento} é de {dimensao}m²")
    

l = float(input("Largura (m): "))
m = float(input("Comprimento (m): "))
area(l,m)