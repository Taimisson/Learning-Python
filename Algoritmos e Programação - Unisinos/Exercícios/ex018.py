# Exercício 18 - Grau C

def calcular_media(ga, gb):
    return(ga * 0.33 + gb * 0.67)

def main():
    try:
        ga = float(input("Informe a nota do Grau A: "))
        gb = float(input("Informe a nota do Grau B: "))

        if ga < 0 or gb < 0:
            raise ValueError("Valores negativos não são permitidos!")

        media = calcular_media(ga, gb)
        
        if media >= 6.0:
            print("Você está aprovado(a) sem necessidade do Grau C!")
        elif media >= 4.0:
            print("Você pode fazer o Grau C.")
        else:
            print("Você está reprovado(a) e não tem direito a fazer o Grau C.")
            
    except ValueError as e:
        print(f"Erro: {e}")
    
if __name__ == "__main__":
    main()