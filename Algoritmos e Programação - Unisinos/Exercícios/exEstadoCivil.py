# Crie um programa que solicita o nome e o estado civil de 20 pessoas pelo teclado. Ao final, imprima apenas o nome das pessoas separadas por estado civil: solteiras, casadas, divorciadas e viúvas (nesta ordem!)

casados = []
solteiros = []
divorciados = []
viúvos = []

for i in range(1,5):
    nome = str(input("Digite o seu nome: "))
    estadoCivil = str(input("Digite o seu estado civil [solteiro(a), casado(a), divorciado(a), viúvo(a)]: ")).lower()
    
    if estadoCivil == "solteiro" or estadoCivil == "solteira": 
        solteiros.append(nome)
    elif estadoCivil == "casado" or estadoCivil == "casada":
        casados.append(nome)
    elif estadoCivil == "divorciado" or estadoCivil == "divorciada":
        divorciados.append(nome)
    elif estadoCivil == "viúvo" or estadoCivil == "viúva":
        viúvos.append(nome)
        
for i in solteiros:
    print(f"Nome: {i} | Estado Civil: Solteiro")
    
for i in casados:
    print(f"Nome: {i} | Estado Civil: Casado")
    
for i in divorciados:
    print(f"Nome: {i} | Estado Civil: Divorciado")

for i in viúvos:
    print(f"Nome: {i} | Estado Civil: Viúvo")
    
    
# nomes = [] 
# estadosCivis = []

# for i in range(1,4):
#     nome = str(input("Digite o seu nome: "))
#     estado_civil = str(input("Digite o seu nome: "))
    
#     nomes.append(nome)
#     estadosCivis.append(estado_civil)
    
# for i, k in zip(nomes, estadosCivis):
#     print(f"Nome: {i} Estado Civil: {k}")
    

