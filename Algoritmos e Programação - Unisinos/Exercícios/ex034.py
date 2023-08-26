# Solicitar 10 times

contador = 0
i = 0

while i < 10:
    time = str(input("Qual time você torce? ")).lower()
    if time == "grêmio":
        contador += 1
    i += 1
    
print(f"Quantidade de torcedores do grêmio: {contador}")

    