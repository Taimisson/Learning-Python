# Soma até 200

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

soma_primos = 0

for num in range(0, 201):
    if eh_primo(num):
        soma_primos += num
        print(num)

print(f"Soma dos números primos: {soma_primos}")
