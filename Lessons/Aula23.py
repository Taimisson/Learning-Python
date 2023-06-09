# Aula 23
# Tratamento de erros

# n = int(input("Número: ")) # "Oito" não aceita
# print(n)

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except:
    print("Infelizmente tivemos um problema :(")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre! Muito obrigado!")