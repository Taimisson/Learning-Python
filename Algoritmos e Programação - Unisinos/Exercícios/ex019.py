# Exercício - Vogal ou Consoante

def main():
    letra = input("Digite uma letra: ").lower()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma única letra.")
    elif letra in ["a", "e", "i", "o", "u"]:
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")

if __name__ == "__main__":
    main()